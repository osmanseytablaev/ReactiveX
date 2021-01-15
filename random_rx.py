from rx import create
import random

number = random.randint(1, 10)
x = int(input("Напиши любое число от 1 до 10: "))


def test_observable(observer, scheduler):
    observer.on_next()


source = create(test_observable)
if x != number:
    print("Ты не угадал лошара было число: ", number)
if x == number:
    source.subscribe(
        on_next=lambda i: print("Ты угадал, молодец!".format(i)),
    )
if x == number:
    m = input("Хочешь продолжить: ")
    if m == "y":
        x = int(input("Напиши любое число от 1 до 10: "))
if x != number:
    m = input("Хочешь продолжить: ")
    if m == "y":
        x = int(input("Напиши любое число от 1 до 10: "))
