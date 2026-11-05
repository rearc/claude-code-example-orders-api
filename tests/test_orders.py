import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from orders_api.handlers import orders


class CreateOrder(unittest.TestCase):
    def test_creates(self):
        status, body = orders.create_order({"item": "widget", "quantity": 2})
        self.assertEqual(status, 201)
        self.assertEqual(body["quantity"], 2)

    def test_rejects_missing_item(self):
        status, _ = orders.create_order({"quantity": 2})
        self.assertEqual(status, 400)


if __name__ == "__main__":
    unittest.main()
