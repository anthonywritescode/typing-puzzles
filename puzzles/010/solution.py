from __future__ import annotations

import json
from typing import Never


def dumps(o: object, **kwargs: Never) -> str:
    return json.dumps(o, separators=(',', ':'))

# ^ library code
# ----------------
# v consuming code


def typed_code(x: list[int]) -> None:
    print(dumps(x, indent=2))  # error at typing time


def untyped_code(x):
    print(dumps(x, indent=2))  # allow this to succeed at runtime for now
