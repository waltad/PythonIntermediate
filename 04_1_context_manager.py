"""Napisz klasę będącą context managerem, która wypisze czas trwania kodu, który zostanie pod nim uruchomiony.

Podpowiedź
W funkcji __enter__ zapisz aktulany timestamp, a w funkcji __exit__ odejmij od aktualnego ten zapisany wcześniej."""

from time import time, sleep


