#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Дан список учащихся 5 "а" класса, в котором указаны фамилии
и рост.Найти рост самого высокого ученика.
"""


def school(**most):
    """Поиск самого высокого ученика"""
    maximum = 0
    z = ""
    for name, height in most.items():
        if height > maximum:
            maximum = height
            z = name
    print(f"Самый высокий ученик {z} имеет рост {maximum} см")


if __name__ == '__main__':
    school(Иван=150, Коля=167, Дима=186, Игорь=177)
