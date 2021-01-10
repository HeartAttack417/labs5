#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти произведение положительных элементов и вывести
# его на экран.

if __name__ == '__main__':
    A = list(map(float, input("Введите список из 10 элементов ").split()))
    summ = 0
    for item in A:
        if item > 0:
            summ += item
    print(summ)
