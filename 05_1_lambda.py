"""Napisz program, który użyje funkcji filter, wypisujący te słowa, które z przekazanej listy słów, są palindromami.
Palindrom to wyrażenie, które czytane zarówno od lewej, jak i od prawej brzmi tak samo. Palindromami będą np. słowa:
inni, kajak, radar."""
import re


def palindromes_finder(words_list):
    new_list = list(filter(lambda word: (word == word[::-1]), words_list))
    return new_list


if __name__ == '__main__':
    text = """Napisz program, który użyje funkcji filter, wypisujący te słowa, które z przekazanej listy słów, są palindromami. Palindrom to wyrażenie, które czytane zarówno od lewej, jak i od prawej brzmi tak samo. Palindromami będą np. słowa: inni, kajak, radar."""
    words = re.split(' |, |\\. |\.|\n', text)

    print(palindromes_finder(words))

    my_list = ["inni", "kajak", "radar", "mama"]
    result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
    print(result)
