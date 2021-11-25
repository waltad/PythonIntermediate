"""Napisz program który używając modułu pickle zapisze do pliku w formacie binarnym obiekt klasy:

from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str

i odczyta go, wypisując na ekran zawartość pól.

Podpowiedź
Użyj funkcji load i dump z pakietu pickle aby zapisać obiekt do pliku."""
from pickle import load, dump
from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str


if __name__ == '__main__':
    # dump(User('Peter', 'Parker'), open('obj.wb', 'wb'))
    # obj = load(open('obj.wb', 'rb'))
    # print(obj)

    obj = User('Kubuś', 'Puchatek')
    with open('data.wb', 'wb') as f:
        dump(obj, f)
    with open('data.wb', 'rb') as f:
        data = load(f)
        print(data)
