"""Shared Meta Marketing API client.

All bundled scripts import from here. Keeps auth, pagination, error
handling, and rate-limit logic in one place so individual scripts stay
small and readable.

Design choices:
- Plain `requests` instead of facebook-business SDK. The SDK pins to
  one API version per release and is heavy. Raw HTTP is transparent
  and lets us upgrade by changing one constant.
- Auto-loads .env from cwd if present (no python-dotenv dependency,
  simple parser handles KEY=value lines).
- Raises MetaAPIError with the full Meta error body on failure so the
  caller can decide what to do (retry, prompt user, abort).
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Any, Iterator

try:
    import requests
except ImportError:
    print(
        "[meta-ads] Missing dependency: requests.\n"
        "  Install it for your OS:\n"
        "    macOS:   python3 -m pip install --user requests\n"
        "    Windows: python  -m pip install --user requests\n"
        "             (or: py -m pip install --user requests)\n"
        "    Linux:   python3 -m pip install --user requests\n"
        "             (add --break-system-packages on Debian/Ubuntu 22+)\n"
        "  Or, from the skill directory: pip install -r requirements.txt\n",
        file=sys.stderr,
    )
    sys.exit(1)


GRAPH_BASE = "https://graph.facebook.com"
DEFAULT_VERSION = "v25.0"

# Rate-limit error subcodes worth backing off on rather than failing immediately.
# 1487742 = ad account rate limit. 2446079 = user rate limit. 1487390 = app rate limit.
RATE_LIMIT_SUBCODES = {1487742, 2446079, 1487390}


class MetaAPIError(RuntimeError):
    """Raised when Meta returns an error response.

    Attributes:
        body: full parsed Meta error body (dict)
        status: HTTP status code
    """

    def __init__(self, body: dict, status: int):
        self.body = body
        self.status = status
        err = body.get("error", {})
        msg = err.get("message", "Unknown Meta API error")
        code = err.get("code", "?")
        sub = err.get("error_subcode", "")
        super().__init__(f"Meta API {status} (code={code}, subcode={sub}): {msg}")


def _load_dotenv(path: Path = Path(".env")) -> None:
    """Minimal .env loader. Lines like KEY=value, # comments, blanks ignored."""
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        # Don't clobber explicit env vars from the shell.
        os.environ.setdefault(key, val)


def get_token() -> str:
    """Return the access token or raise with a clear setup pointer."""
    _load_dotenv()
    tok = os.environ.get("META_ACCESS_TOKEN")
    if not tok:
        raise RuntimeError(
            "META_ACCESS_TOKEN not set. Add it to .env or export it. "
            "If you don't have one yet, see references/setup.md."
        )
    return tok


def get_default_account() -> str | None:
    """Return the default ad account ID (act_xxxx) if set, else None."""
    _load_dotenv()
    return os.environ.get("META_AD_ACCOUNT_ID")


def get_version() -> str:
    _load_dotenv()
    return os.environ.get("META_API_VERSION", DEFAULT_VERSION)


def _request(
    method: str,
    path: str,
    *,
    params: dict | None = None,
    data: dict | None = None,
    max_retries: int = 3,
) -> dict:
    """Make an authenticated request. Handles retries on rate limits.

    `path` should start with the object ID or edge, e.g.
    "act_123/insights" or "1234567890". Don't include the leading slash
    or the version - those are added here.
    """
    version = get_version()
    url = f"{GRAPH_BASE}/{version}/{path.lstrip('/')}"
    params = dict(params or {})
    params["access_token"] = get_token()

    for attempt in range(max_retries):
        try:
            resp = requests.request(method, url, params=params, data=data, timeout=60)
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
            continue

        if resp.ok:
            return resp.json()

        # Try to parse the error body. If it's JSON and tells us this
        # was a rate limit, back off and retry.
        try:
            body = resp.json()
        except ValueError:
            body = {"error": {"message": resp.text or f"HTTP {resp.status_code}"}}

        sub = body.get("error", {}).get("error_subcode")
        if sub in RATE_LIMIT_SUBCODES and attempt < max_retries - 1:
            wait = 60 * (attempt + 1)  # back off in minutes; ad rate limits are slow
            print(
                f"[meta_client] Rate limit hit (subcode {sub}), sleeping {wait}s",
                file=sys.stderr,
            )
            time.sleep(wait)
            continue

        raise MetaAPIError(body, resp.status_code)

    # Shouldn't reach here, but mypy.
    raise RuntimeError("Exhausted retries without success or error")


def get(path: str, params: dict | None = None) -> dict:
    return _request("GET", path, params=params)


def post(path: str, data: dict, params: dict | None = None) -> dict:
    return _request("POST", path, params=params, data=data)


def delete(path: str, params: dict | None = None) -> dict:
    return _request("DELETE", path, params=params)


def paginate(path: str, params: dict | None = None, max_pages: int = 100) -> Iterator[dict]:
    """Yield each item across paginated results.

    Meta returns {"data": [...], "paging": {"next": url, "cursors": {...}}}.
    We follow `paging.next` until exhausted or we hit max_pages (safety).
    """
    page = 0
    next_url: str | None = None
    current_path: str | None = path
    current_params = dict(params or {})

    while page < max_pages:
        if next_url:
            # `next` is a fully-formed URL with token already embedded.
            try:
                resp = requests.get(next_url, timeout=60)
            except requests.RequestException:
                break
            if not resp.ok:
                # Surface the error rather than swallowing it.
                try:
                    body = resp.json()
                except ValueError:
                    body = {"error": {"message": resp.text}}
                raise MetaAPIError(body, resp.status_code)
            data = resp.json()
        else:
            data = get(current_path, current_params)

        for item in data.get("data", []):
            yield item

        next_url = data.get("paging", {}).get("next")
        if not next_url:
            break
        page += 1


def normalize_account_id(account_id: str | None) -> str:
    """Accept either '1234567890' or 'act_1234567890' and return the act_ form."""
    if not account_id:
        account_id = get_default_account()
    if not account_id:
        raise RuntimeError(
            "No ad account ID provided and META_AD_ACCOUNT_ID not set. "
            "Pass --account-id or set the env var."
        )
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    return account_id


def print_json(obj: Any) -> None:
    """Standard JSON output for all scripts. Indented for readability."""
    json.dump(obj, sys.stdout, indent=2, ensure_ascii=False, default=str)
    sys.stdout.write("\n")


def start_async_insights_job(account_id: str, params: dict) -> str:
    """Start an async insights report. Returns the report run ID.

    Use this when a sync insights query would time out - e.g., very long
    date ranges or many breakdowns. Poll with `poll_async_job`.
    """
    account_id = normalize_account_id(account_id)
    resp = post(f"{account_id}/insights", data=params)
    run_id = resp.get("report_run_id")
    if not run_id:
        raise RuntimeError(f"Async insights job did not return a run_id: {resp}")
    return run_id


def poll_async_job(run_id: str, poll_interval: int = 5, timeout: int = 1800) -> dict:
    """Poll an async report until done. Returns the final status object.

    Raises if the job fails or times out. On success, the caller should
    GET /{run_id}/insights to fetch the actual data.
    """
    elapsed = 0
    while elapsed < timeout:
        status = get(run_id)
        s = status.get("async_status")
        if s == "Job Completed":
            return status
        if s in ("Job Failed", "Job Skipped"):
            raise RuntimeError(f"Async insights job {run_id} ended with status: {s}")
        time.sleep(poll_interval)
        elapsed += poll_interval
    raise TimeoutError(f"Async insights job {run_id} did not finish within {timeout}s")
