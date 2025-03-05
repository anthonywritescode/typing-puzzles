from __future__ import annotations

from typing import Literal
from typing import NamedTuple
from typing import Self


Operation = Literal['avg', 'max', 'min', 'sum']
Stat = Literal['duration', 'size']


class Metric(NamedTuple):
    operation: Operation
    stat: Stat

    @classmethod
    def from_s(cls, s: str) -> Self:
        op, stat = s.split(':', 1)
        return cls(op, stat)


print(Metric.from_s('avg:size'))
