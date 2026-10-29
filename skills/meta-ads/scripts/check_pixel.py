#!/usr/bin/env python3
"""Check which Meta Pixel IDs actually load on each page of a funnel.

  python scripts/check_pixel.py --pixel-id 1234567890123456 \
      https://example.com/ https://checkout.example.com/product

For every URL it fetches the HTML (following redirects, cache-busted) and reports every
fbq('init', '<id>') and every <noscript> tr?id=<id> it finds, then flags:
  - MISSING   the expected pixel is not on the page
  - EXTRA     another pixel ID also loads (double counting, or an old pixel left behind)
  - SUSPECT   an ID that is 15-16 digits like a pixel but is the ad account ID
              (the classic paste mistake; pass --ad-account-id to detect it)

Limits, on purpose:
  - Only server-rendered HTML is seen. A pixel injected later by a tag manager or by JS won't show:
    confirm those in Events Manager -> Test events.
  - It proves the pixel is INSTALLED, not that events FIRE. Meta suppresses events from headless
    browsers, so the final proof is always Test events with a real browser/phone.
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.request

INIT = re.compile(r"""fbq\(\s*['"]init['"]\s*,\s*['"](\d{10,20})['"]""")
NOSCRIPT = re.compile(r"facebook\.com/tr\?id=(\d{10,20})")


def fetch(url: str) -> str:
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}_pxcheck={int(time.time())}",
                                 headers={"User-Agent": "Mozilla/5.0 (pixel-check)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--pixel-id", required=True, help="the pixel (dataset) ID that should be on every page")
    ap.add_argument("--ad-account-id", default=None, help="numeric ad account ID, to catch it pasted as a pixel ID")
    args = ap.parse_args()
    acct = (args.ad_account_id or "").removeprefix("act_")

    results, ok = [], True
    for url in args.urls:
        try:
            html = fetch(url)
        except Exception as e:  # noqa: BLE001
            results.append({"url": url, "error": f"{type(e).__name__}: {e}"})
            ok = False
            continue
        inits = sorted(set(INIT.findall(html)))
        noscripts = sorted(set(NOSCRIPT.findall(html)))
        flags = []
        if args.pixel_id not in inits:
            flags.append("MISSING: expected pixel not initialised on this page")
        extra = [i for i in inits if i != args.pixel_id]
        if extra:
            flags.append(f"EXTRA: other pixel IDs also load: {extra}")
        if acct and acct in set(inits) | set(noscripts):
            flags.append("SUSPECT: the ad account ID was pasted where the pixel ID belongs")
        if noscripts and args.pixel_id not in noscripts:
            flags.append("NOSCRIPT MISMATCH: the <noscript> fallback carries a different ID")
        ok = ok and not flags
        results.append({"url": url, "fbq_init": inits, "noscript_ids": noscripts, "flags": flags or ["OK"]})

    print(json.dumps({"ok": ok, "pixel_id": args.pixel_id, "pages": results}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
