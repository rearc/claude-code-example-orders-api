# Generated from openapi.json by scripts/generate.py. Do not edit.
from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    id: str
    item: str
    quantity: int
