from __future__ import annotations

import builtins
import dataclasses


class Base:
    ...


class C(Base):
    ...


class D(Base):
    ...


_MAP = {'C': C, 'D': D}


@dataclasses.dataclass
class M:
    type: str

    def get_t(self) -> builtins.type[Base]:
        return _MAP[self.type]
