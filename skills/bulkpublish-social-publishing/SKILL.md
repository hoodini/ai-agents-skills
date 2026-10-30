---
name: bulkpublish-social-publishing
description: "Use when an AI agent must adapt, review, schedule, or publish approved social media content through BulkPublish's API or hosted MCP."
---

# BulkPublish Social Publishing

Use this skill for the final operational stage of a social-media workflow: moving approved content into scheduled or published posts across multiple platforms. BulkPublish provides the API and hosted MCP that perform the external publishing operation.

## References

- API repository: https://github.com/azeemkafridi/bulkpublish-api
- MCP documentation: https://app.bulkpublish.com/docs
- Hosted MCP endpoint: https://mcp.bulkpublish.com/mcp
- Source social-media skills: https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills

## Instructions

1. Gather the approved copy, media, destination platforms and accounts, timezone, and requested publish time.
2. Adapt the content to each platform while preserving approved claims, links, disclosures, consent, and brand constraints.
3. Show the exact per-platform payload, media, account targets, and schedule to the user.
4. Wait for explicit approval of that exact payload and target set before making any create, schedule, or publish call.
5. Use BulkPublish's API or hosted MCP to execute the approved operation.
6. Retrieve each result and report its platform, account, status, schedule, identifier, public URL, and errors.

## Guardrails

- Treat publishing and scheduling as external side effects; never infer approval from an earlier draft.
- Never invent account identifiers, media URLs, permissions, delivery results, or analytics.
- If a call times out, retrieve its status before retrying to prevent duplicate posts.
- Report partial success per platform and leave failed targets unsent until the user approves a retry.
- Preserve platform disclosures, opt-outs, copyright notes, and human review requirements.

## Output Format

Return a compact status table with platform, account, operation, status, scheduled time, identifier, public URL when available, and unresolved follow-up actions.
