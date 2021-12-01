"""Napisz program, który używając wyrażeń regularnych, sprawdzi czy podany numer telefonu jest poprawny.
Poprawne numery to:

48123456789
+48123456789
0048123456789
czyli na początku albo samo 48, albo +48 albo 0048 a potem 9 cyfr."""

import re

pattern = r"(\+|00)?48\d{9}"
tests = ('48123456789', '+48123456789', '0048123456789')


if __name__ == '__main__':
    for test in tests:
        print(test, bool(re.fullmatch(pattern, test)))

    print()
# lub
    p = re.compile(pattern)
    for test in tests:
        print(test, bool(p.fullmatch(test)))
