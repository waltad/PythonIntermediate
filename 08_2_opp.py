"""Zaimplementuj obiektowo mechanizm obsługi dostępów dla użytkowników. Stwórz klasę User która będzie przechowywać
aktualne dostępy oraz historię zmian. Zadbaj o odpowiednią hermetyzację danych oraz dostarcz metody:

grant_permission
revoke_permission
get_first_permissions_change
get_permissions_change_history
Ponad to pozwól na przypisanie do użytkownika listy dostępów. Użyj enuma aby zdefiniować dostępy.
(Odpowiedz sobie na pytania: dlaczego potrzebne jest to .copy() i jak zmienić kod, żeby się go pozbyć?)"""

from enum import Enum, auto
from typing import Set, List
from datetime import datetime


class Permission(Enum):
    READ = auto()
    WRITE = auto()


class PermissionChange:
    def __init__(self, _from: Set[Permission], _to: Set[Permission]):
        self._from = _from
        self._to = _to
        self.datetime = datetime.now()

    def __str__(self):
        return f"{self._from} -> {self._to} at {self.datetime}"

    def __repr__(self):
        return str(self)


class User:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.__permissions: Set[Permission] = set()
        self.__permission_changes: List[PermissionChange] = []

    @property
    def permissions(self) -> Set[Permission]:
        return self.__permissions

    @permissions.setter
    def permissions(self, permissions: Set[Permission]):
        self.__permission_changes.append(PermissionChange(self.__permissions.copy(), permissions.copy()))
        self.__permissions = permissions

    def grant_permission(self, permission: Permission):
        old_permissions = self.__permissions.copy()
        self.__permissions.add(permission)
        self.__permission_changes.append(PermissionChange(old_permissions, self.__permissions.copy()))

    def revoke_permission(self, permission: Permission):
        old_permissions = self.__permissions.copy()
        self.__permissions.remove(permission)
        self.__permission_changes.append(PermissionChange(old_permissions, self.__permissions.copy()))

    def get_first_permissions_change(self) -> PermissionChange:
        return self.__permission_changes[0]

    def get_permissions_change_history(self) -> List[PermissionChange]:
        return self.__permission_changes


if __name__ == '__main__':
    user = User('Karol', 'Mataszczyk')

    user.grant_permission(Permission.WRITE)
    user.grant_permission(Permission.READ)
    user.revoke_permission(Permission.WRITE)

    print("First permission change: ", user.get_first_permissions_change())

    print("All permissions changes: ")

    for change in user.get_permissions_change_history():
        print(change)
