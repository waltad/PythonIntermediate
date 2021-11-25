"""1. Napisz dekorator, który pozwoli wykonać kod dekorowanej funkcji tylko w dzień (między 7 a 22).
Do określenia aktualnej godziny użyj moduły datetime.
1a. Napisz podobny dekorator, jak wyżej, ale spraw by mógł on przyjmować w argumentach godziny, w których funkcja jest
niedostępna.
2. Napisz dekorator, który pokaże godzinę, minutę i sekundę przed wywołaniem kodu dekorowanej funkcji oraz po wywołaniu
kodu dekorowanej funkcji."""

from datetime import datetime


def check_time(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 22:
            func()
    return wrapper


def check_time_set(from_=7, to_=22):
     def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour <= to_:
                func()
        return wrapper
     return dec


def before_after_time(func):
    def wrapper():
        print(datetime.now().strftime('%H:%M:%S'))
        result = func()
        print(datetime.now().strftime('%H:%M:%S'))
        return result
    return wrapper


@check_time
def say_something():
    print('Hello!')


@check_time_set(15, 20)
def say_something_set():
    print('The time is set correctly.')


@before_after_time
def say_something_meanwhile():
    print('Have a good time!')


if __name__ == '__main__':
    say_something()
    say_something_set()
    say_something_meanwhile()
