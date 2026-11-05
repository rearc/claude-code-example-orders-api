"""Generate src/orders_api/generated/models.py from openapi.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPES = {"string": "str", "integer": "int", "number": "float", "boolean": "bool"}

spec = json.loads((ROOT / "openapi.json").read_text())
lines = [
    "# Generated from openapi.json by scripts/generate.py. Do not edit.",
    "from dataclasses import dataclass",
    "from typing import Optional",
    "",
]
for name, schema in spec["components"]["schemas"].items():
    required = set(schema.get("required", []))
    props = schema["properties"].items()
    lines += ["", "@dataclass", f"class {name}:"]
    for field, p in sorted(props, key=lambda kv: kv[0] not in required):
        t = TYPES[p["type"]]
        lines.append(f"    {field}: {t}" if field in required else f"    {field}: Optional[{t}] = None")
    lines.append("")
(ROOT / "src/orders_api/generated/models.py").write_text("\n".join(lines))
print("wrote src/orders_api/generated/models.py")
