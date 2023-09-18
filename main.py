"""2. Написать функцию, которая принимает два целочисленных списка и возвращает True, если первые или последние
элементы данных списков равны. Оба списка содержат 1 или
более элементов."""

from random import randint


def main():
    while True:
        numbers1 = []
        numbers2 = []

        for i in range(10):
            numbers1.append(randint(-10, 10))
        for j in range(10):
            numbers2.append(randint(-10, 10))

        if numbers1[0] == numbers2[0] or numbers1[-1] == numbers2[-1]:
            print('True')
            print(numbers1)
            print(numbers2)
        else:
            print('False')
            print(numbers1)
            print(numbers2)
        if numbers1[0] == numbers2[0] or numbers1[-1] == numbers2[-1]: break


main()