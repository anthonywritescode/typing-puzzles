from __future__ import annotations

from typing import Any


class User:
    ...


class NAdmin:
    def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError()


class NObject[T]:
    def __init__(self, n: T) -> None:
        self._n = n

    def _get_field_value(self, field: str) -> Any:
        pass


class Post(NObject[NAdmin]):
    def __init__(self, n: NAdmin) -> None:
        super().__init__(n)
        self._user_id = self._get_field_value('user')
        self._user: User | None = None

    @property
    def user(self) -> User:
        if self._user is None:
            self._user = self._n.get_user_by_id(self._user_id)
        return self._user
