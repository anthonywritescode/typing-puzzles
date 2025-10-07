from __future__ import annotations

import json


def dumps(o, **kwargs):
    kwargs.setdefault('separators', (',', ':'))
    return json.dumps(o, **kwargs)

# ^ library code
# ----------------
# v consuming code


def typed_code(x: list[int]) -> None:
    print(dumps(x, indent=2))  # error at typing time


def untyped_code(x):
    print(dumps(x, indent=2))  # allow this to succeed at runtime for now
