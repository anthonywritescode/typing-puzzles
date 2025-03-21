from __future__ import annotations

from typing import TypedDict


class SomeTypedDict(TypedDict):
    some_key: str


def some_func() -> SomeTypedDict:
    return {'some_key': 'some_value'}


def other_func(cond: bool) -> None:
    _ = some_func() if cond else {}
