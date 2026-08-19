from __future__ import annotations

_MISSING = sentinel('_MISSING')  # noqa: F821


def do(x: int | None | _MISSING = _MISSING) -> None:
    if x is _MISSING:
        print('no `x` was passed!')
    elif x is None:
        print('`x` was explicitly passed as `None`')
    else:
        print(f'x**2 is {x**2}')


do()
do(None)
do(9001)
# do('no')  # should be an error!
