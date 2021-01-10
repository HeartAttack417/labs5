#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) сумму положительных элементов списка;
# 2) произведение элементов списка, расположенных между максимальным по модулю и
# минимальным по модулю элементами.
# Упорядочить элементы списка по убыванию.

import sys

if __name__ == '__main__':
    a = list(map(float, input("Введите список из 10 элементов ").split()))
    a.sort(reverse=True)
    print(a)
    summ = 0
    proiz = 1
    for item in a:
        if item > 0:
            summ += item
    print(summ)

    a_min = a_max = a[0]
    i_min = i_max = 0
    for i, item in enumerate(a):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item

    for i, item in enumerate(a):
        if i_max < i < i_min:
            proiz *= item
    print(proiz)
