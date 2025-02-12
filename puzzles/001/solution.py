from __future__ import annotations

from typing import NotRequired
from typing import TypedDict


class _SomeFunctionKwargs(TypedDict):
    x: int
    y: NotRequired[str]


def some_function(
        x: int,
        *,
        y: str = 'default',
        z: float | None = None,
) -> None:
    ...


def other_function(x: int, *, do_y: bool) -> None:
    kwargs: _SomeFunctionKwargs = {'x': x}
    if do_y:
        kwargs['y'] = 'indeed!'
    some_function(**kwargs, z=None)
