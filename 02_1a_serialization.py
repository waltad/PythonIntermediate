"""Funkcja get_avg nie jest odporna na sytuację, w której dostanie jako parametr coś innego niż stringa, np.:

def get_avg(*args):
    return sum(args) / len(args)

get_avg(1, 3, 'a')
Rzuci wyjątkiem:

Traceback (most recent call last):
  File "/home/mmazurek/testy3/main.py", line 16, in <module>
    get_avg(1, 3, 'a')
  File "/home/mmazurek/testy3/main.py", line 5, in get_avg
    return sum(args) / len(args)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
Popraw ją tak, by omijała zmienne innego typu niż int lub float."""


def get_avg(*args):
    allowed_types = (int, float)
    # new_args = [x for x in args if type(x) in allowed_types]
    new_args = [x for x in args if isinstance(x, allowed_types)]
    return sum(new_args) / len(new_args)


if __name__ == '__main__':
    print(get_avg(1, 3, 'a', 5, 3, 'b'))
