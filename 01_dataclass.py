"""Dataclass
Zadanie 1
Stwórz klasę korzystając z dataclass, która:
* będzie posiadać 4 argumenty konstruktora:
   - first_int o typie int
   - multiplier o typie int
   - list_of_ints o typie listy intów
   - second_int o typie int i wartości domyślnej 0
* będzie posiadać 1 pole:
   - calculated_val o typie float
* wartość pola calculated_val to (first_int * multiplier * sum(list_of_ints)) - second_int
* porównywanie obiektów ma być oparte tylko o wartości pola calculated_val
* tak stworzony obiekt powinien być callable i w wyniku wykonania, zwracać wartość pola calculated_val
* forma wyświetlania obieku przez funkcję print ma być taka, jak niżej w przykładach
Przykład użycia obiektu:
... t = Test(2, 2, [2, 1], 9)
... print(t)
... print(t())
...
Test(calculated_val=3)
3

... t = Test(3, 5, [2, 2], 1)
... print(t)
... print(t())
...
Test(calculated_val=59)
59

... t1 = Test(3, 2, [2, 2], 1)
... t2 = Test(4, 1, [2, 4], 1)
...
... print(t1 == t2)
...
...
True
Podpowiedź
Potrzebujesz skorzystać z elementów takich jak: InitVar, funkcja field, a dokładniej jej argumenty default i init. Do
tego metoda post_init."""
from dataclasses import dataclass, InitVar, field
from typing import List


@dataclass
class Test:
    first_int: InitVar[int]
    multiplier: InitVar[int]
    list_of_ints: InitVar[List[int]]
    second_int: InitVar[int] = field(default=0)
    calculated_val: float = field(init=False)

    def __post_init__(self, first_int: int, multiplier: int, list_of_ints: List[int], second_int: int):
        self.calculated_val = (first_int * multiplier * sum(list_of_ints)) - second_int

    def __call__(self, *args, **kwargs):
        return self.calculated_val


if __name__ == '__main__':
    t = Test(2, 2, [2, 1], 9)
    print(t)
    print(t())

    t = Test(3, 5, [2, 2], 1)
    print(t)
    print(t())

    t1 = Test(3, 2, [2, 2], 1)
    t2 = Test(4, 1, [2, 4], 1)
    print(t1 == t2)
