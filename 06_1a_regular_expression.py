"""Weź ten sam tekst, co w zadaniu wyżej i napisz program, używając wyrażeń regularnych, który usunie wszystkie cyfry
z tekstu."""
import re

text = "test43543lfdsfdsfl534543fdgl432fr"
pattern = r"\d+"
# lub
pattern2 = r"[a-z]+"
p = re.compile(pattern2)


if __name__ == '__main__':
    print(re.sub(pattern, '', text))
# lub
    print(''.join(p.findall(text)))
