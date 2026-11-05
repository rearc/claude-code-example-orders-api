---
paths:
  - "src/orders_api/handlers/**"
---
# Handlers
- Validate input with the generated models in `orders_api.generated.models`; don't re-declare fields.
- Return `(status, body)` tuples; never raise for a client error.
- Every handler has a test in `tests/` covering one success and one client error.
