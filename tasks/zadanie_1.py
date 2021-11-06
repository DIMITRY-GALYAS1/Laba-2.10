#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Решить поставленную задачу:
написать функцию, вычисляющую среднее геометрическое
своих аргументов a1, a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение  None
"""


# Вычисляет среднее геометрическое
def average(*arg):

    if arg:
        g = 1.0

        for i in arg:
            g *= i
        g = g ** (1/len(arg))

        return g
    else:
        return None


if __name__ == '__main__':

    print("Введите числа в массив через пробел: ")
    mas = list(map(float, input().split()))
    print(average(*mas))
