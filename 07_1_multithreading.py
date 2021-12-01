"""Napisz program, który posortuje liczby, używając algorytmu SleepSort.

UWAGA: Ten algorytm to ciekawostka, nie jest on ani rzetelnym ani wydajnym rozwiązaniem!

Polega on na wykorzystaniu funkcji sleep(). A dokładnie:
Dla każdej z tych liczb tworzymy osobny wątek i usypiamy go funkcją sleep na czas proporcjonalny do wartości danej
liczby. Wiadomo, że najszybciej skończy się wykonywać wątek, który został uśpiony na najmniejszą ilość czasu a więc ten,
który miał najmniejszą liczbę. Po funkcji sleep można dodawać te liczby do kolekcji w ten sposób otrzymując efekt
sortowania."""
import threading
from time import sleep

numbers_to_sort = [4, 2, 6, 9, 3]

sorted = []
threads = []


def sort_func(num):
    sleep(num * 0.1)
    sorted.append(num)


for x in numbers_to_sort:
    t = threading.Thread(target=sort_func, args=(x,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

if __name__ == '__main__':
    print(sorted)
