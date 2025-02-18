from __future__ import annotations


class C:
    def name(self) -> str:
        return 'I am C!'


def f1(x: str | None) -> None: ...


def f2(c: C | None) -> None:
    f1(c and c.name())
