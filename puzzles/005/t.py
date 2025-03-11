from __future__ import annotations


def flatten(lst):
    def _helper(lst):
        for item in lst:
            if isinstance(item, list):
                yield from _helper(item)
            else:
                yield item
    return [item for item in _helper(lst)]


print(flatten([[[1], [2, 3]], [4]]))
