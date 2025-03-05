from __future__ import annotations

import enum
from typing import Literal
from typing import NamedTuple
from typing import Self


Operation = Literal['avg', 'max', 'min', 'sum']


class EOperation(enum.StrEnum):
    AVG = 'avg'
    MAX = 'max'
    MIN = 'min'
    SUM = 'sum'


Stat = Literal['duration', 'size']


class EStat(enum.StrEnum):
    DURATION = 'duration'
    SIZE = 'size'


class Metric(NamedTuple):
    operation: Operation
    stat: Stat

    @classmethod
    def from_s(cls, s: str) -> Self:
        op, stat = s.split(':', 1)
        return cls(EOperation(op).value, EStat(stat).value)


print(Metric.from_s('avg:size'))
