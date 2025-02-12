from __future__ import annotations


def some_function(
        x: int,
        *,
        y: str = 'default',
        z: float | None = None,
) -> None:
    ...


def other_function(x: int, *, do_y: bool) -> None:
    kwargs = {'x': x}
    if do_y:
        kwargs['y'] = 'indeed!'
    some_function(**kwargs, z=None)
