from __future__ import annotations

from typing import get_args
from typing import Literal
from typing import NamedTuple
from typing import Self
from typing import TypeIs


Operation = Literal['avg', 'max', 'min', 'sum']
_Operation_values: frozenset[Operation] = frozenset(get_args(Operation))


def is_operation(s: str) -> TypeIs[Operation]:
    return s in _Operation_values


Stat = Literal['duration', 'size']
_Stat_values: frozenset[Stat] = frozenset(get_args(Stat))


def is_stat(s: str) -> TypeIs[Stat]:
    return s in _Stat_values


class Metric(NamedTuple):
    operation: Operation
    stat: Stat

    @classmethod
    def from_s(cls, s: str) -> Self:
        op, stat = s.split(':', 1)
        if not is_operation(op):
            raise ValueError(op)
        if not is_stat(stat):
            raise ValueError(stat)
        return cls(op, stat)


print(Metric.from_s('avg:size'))
