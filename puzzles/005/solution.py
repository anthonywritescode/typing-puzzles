from __future__ import annotations

from collections.abc import Generator

type _RList[U] = list[U | _RList[U]]


def flatten[T](lst: _RList[T]) -> list[T]:
    def _helper(lst: _RList[T]) -> Generator[T]:
        for item in lst:
            if isinstance(item, list):
                yield from _helper(item)
            else:
                yield item
    return [item for item in _helper(lst)]


x: _RList[int] = [[[1], [2, 3]], [4]]
print(flatten(x))
