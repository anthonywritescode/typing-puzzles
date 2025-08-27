from __future__ import annotations


class _Option[T]:
    ...


class _PartialOption[T]:
    def default(self, o: T) -> _Option[T]:
        raise NotImplementedError


def make_option[T](tp: type[T]) -> _PartialOption[T]:
    raise NotImplementedError


# ok
make_option(str).default('')
# ok
make_option(int).default(0)
# should be error!
make_option(str).default(0)
