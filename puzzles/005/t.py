from __future__ import annotations

from collections.abc import Generator


def flatten[T](lst) -> list[T]:
    def _helper(lst) -> Generator[T]:
        for item in lst:
            if isinstance(item, list):
                yield from _helper(item)
            else:
                yield item
    return [item for item in _helper(lst)]


print(flatten([[[1], [2, 3]], [4]]))
