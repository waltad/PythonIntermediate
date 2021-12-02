"""Jak wiesz z zajęć, klasa abstrakcyjna służy do odwzorowania obiektów które same w sobie nie istnieją, ale są bazą do
innych obiektów. Np. nie jesteś w stanie stworzyć zwierzęcia, bo zwyczajnie nie wiesz co to za zwierze. Stwórz więc
klasę abstrakcyjną odwzorowującą tę sytuację oraz klasy potomne, implementujące metodą zwracającą dźwięk wydawany przez
konkretne zwierze. Hierarchia do zaimplementowania: Animal, Lion, Bird - Sparrow
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_voice(self):
        pass


class Lion(Animal):
    def __init__(self, species):
        self.species = species

    def get_voice(self):
        return 'roar roar!!!'


class Bird(Animal):
    def __init__(self, species):
        self.species = species

    def get_voice(self):
        return 'ćwir ćwir'


class Sparrow(Bird):
    def __init__(self, species):
        super().__init__(species)
        

if __name__ == '__main__':
    lion = Lion('Mufasa')
    print(lion.species)
    print(lion.get_voice())

    sparrow = Sparrow('Jack')
    print(sparrow.species)
    print(sparrow.get_voice())
