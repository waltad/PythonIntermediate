"""Zadanie 1
Masz plik tekstowy z zawartością:
{
   "right_side":[
      3,
      5,
      3,
      6,
      4,
      2,
      3,
      6,
      8,
      4,
      3,
      2
   ],
   "left_side":[
      1.2,
      4.3,
      5.4,
      6.9,
      9.9,
      7.2
   ]
}
Napisz program, który wypisze średnią z liczb z pola "right_side", średnią z pola "left_side" oraz średnią z obu pól.
Podpowiedź
Użyj funkcji open, żeby otworzyć plik, a następnie funkcji load, żeby skonwertować dane JSON na format Pythona."""
from json import load


def get_avg(*args):
    return sum(args) / len(args)


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = load(f)
        print('Right side:', get_avg(*data['right_side']))
        print('Left side:', get_avg(*data['left_side']))
        print('All:', get_avg(*data['right_side'], *data['left_side']))
        # print(get_avg(1, 3, 'a'))
