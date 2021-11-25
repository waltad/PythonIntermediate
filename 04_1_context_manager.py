"""Napisz klasę będącą context managerem, która wypisze czas trwania kodu, który zostanie pod nim uruchomiony.

Podpowiedź
W funkcji __enter__ zapisz aktulany timestamp, a w funkcji __exit__ odejmij od aktualnego ten zapisany wcześniej."""

from time import time, sleep


class TimeIt:
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, type, value, traceback):
        total = time() - self.start
        print("{}[s]".format(total))


if __name__ == '__main__':
    with TimeIt():
        sleep(1)
