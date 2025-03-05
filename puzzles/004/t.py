from __future__ import annotations

from typing import ClassVar


class Abstract:
    name: ClassVar[str]

    @classmethod
    def tag(cls) -> str:
        return f'<{cls.name}>'

    def hello(self) -> None:
        print(f'{self.tag()} hello hello')


class ConcreteGood(Abstract):
    name = 'good'


class ConcreteBad(Abstract):
    pass  # missing `name`!


ConcreteGood().hello()
ConcreteBad().hello()
