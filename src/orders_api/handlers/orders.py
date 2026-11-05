from dataclasses import asdict
from uuid import uuid4

from orders_api.generated.models import Order

ORDERS: dict[str, Order] = {}


def list_orders():
    return 200, [asdict(o) for o in ORDERS.values()]


def create_order(body: dict):
    try:
        order = Order(id=str(uuid4()), item=body["item"], quantity=int(body["quantity"]))
    except (KeyError, TypeError, ValueError):
        return 400, {"error": "item and quantity are required"}
    if order.quantity < 1:
        return 400, {"error": "quantity must be at least 1"}
    ORDERS[order.id] = order
    return 201, asdict(order)
