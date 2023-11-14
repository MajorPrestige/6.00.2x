#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:17:24 2023

@author: prestige
"""

def fibonacci_dynamic_programming(n):
    # Создаем массив для сохранения промежуточных результатов
    fib_array = [0] * (n + 1)

    # Известные значения для базовых случаев
    fib_array[0] = 0
    fib_array[1] = 1

    # Заполняем массив значениями Фибоначчи от 2 до n
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]

    return fib_array[n]


n = 10
result = fibonacci_dynamic_programming(n)
print(f"Число Фибоначчи для n={n}: {result}")