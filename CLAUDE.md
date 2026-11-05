# orders-api

HTTP API for orders. Python 3.11+, standard library only.

## Layout
- `openapi.json`: the API contract. Other repos (orders-web) build against it. Change it first.
- `src/orders_api/handlers/`: one module per resource.
- `src/orders_api/generated/`: generated from `openapi.json` by `scripts/generate.py`. Never edit by hand.
- `tests/`: unittest.

## Commands
- Test: `python3 -m unittest discover -s tests`
- Regenerate models after changing `openapi.json`: `python3 scripts/generate.py`

## Conventions
- A contract change is a breaking change unless it only adds optional fields. Say which in the PR.
