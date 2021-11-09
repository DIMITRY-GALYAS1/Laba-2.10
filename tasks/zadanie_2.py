#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее гармоническое
своих аргументов a1, a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


def average(*x):
    """Поиск среднего гармонического"""
    summa = 0
    if x:
        for i in x:
            if i == 0:
                return None
            else:
                summa += 1 / float(i)
        z = 1 / (1 / len(x) * summa)
        return z
    else:
        return None


if __name__ == '__main__':

    print("Введите числа в массив через пробел: ")
    mas = list(map(float, input().split()))
    print(average(*mas))
