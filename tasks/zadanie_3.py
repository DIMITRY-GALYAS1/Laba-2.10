#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Дан список учащихся 5 "а" класса, в котором указаны фамилии
и рост.Найти самого высокого ученика и вывести его.
"""


def school(**most):
    """Поиск самого высокого ученика"""
    maximum = 0
    z = ""
    for name, height in most.items():
        if height > maximum:
            maximum = height
            z = name
    return f"Самый высокий ученик {z} имеет рост {maximum} см"


if __name__ == '__main__':
    print(school(Иван=150, Коля=167, Дима=186, Игорь=177))
