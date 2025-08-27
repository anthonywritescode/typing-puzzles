from __future__ import annotations


class _Option[T]:
    ...


def make_option[T](tp: type[T], *, default: T) -> _Option[T]:
    raise NotImplementedError


# ok
make_option(str, default='')
# ok
make_option(int, default=0)
# should be error!
make_option(str, default=0)
