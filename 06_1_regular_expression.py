"""Wyciągnij, korzystając z wyrażeń regularnych, z zadanego tekstu, wszystkie liczby.

Np., dla "test43543lfdsfdsfl534543fdgl432fr" będą to:
43543
534543
432
Podpowiedź
Użyj tokenu "\d" określającego cyfrę oraz znaku + znaczącego "jeden lub wiecej znaków."""
import re

text = "test43543lfdsfdsfl534543fdgl432fr"
pattern = r"\d+"
match = re.findall(pattern, text)
# lub
p = re.compile(pattern)


if __name__ == '__main__':
    print(match)
    print()
    # lub
    for number in p.findall(text):
        print(number)
    print()
    # lub
    iter = re.finditer(pattern, text)
    for elem in iter:
        print(elem)
