---
name: add-endpoint
description: Add an endpoint to orders-api, from contract to handler to test. Use when asked to add or change an API endpoint or field.
---
# Add an endpoint
1. Add the path and any schema to `openapi.json`.
2. Run `python3 scripts/generate.py` to regenerate `src/orders_api/generated/`.
3. Add the handler in `src/orders_api/handlers/`.
4. Add a test in `tests/` (one success, one client error) and run the tests.
5. If the contract changed, note it for orders-web: which fields, breaking or not.
