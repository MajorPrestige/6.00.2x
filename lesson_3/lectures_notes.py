#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:24:25 2023

@author: prestige
"""


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    if not L:
        return float('NaN')

    strings_length = [len(item) for item in L]
    mean = sum(strings_length) / len(strings_length)
    squared_dev = [(l-mean)**2 for l in strings_length]
    variance = sum(squared_dev) / len(L)
    return variance**0.5


L = ['apples', 'oranges', 'kiwis', 'pineapples']
# print(stdDevOfLengths(L))


a = [10, 4, 12, 15, 20, 5]
mean = sum(item for item in a) / len(a)
deviation = (sum((item-mean)**2 for item in a) / len(a))**0.5
coefficient_of_variation = deviation / mean
print(coefficient_of_variation)


#%%

import numpy as np
import matplotlib.pyplot as plt

# Параметри експоненційного розподілення
lmbda = 1 / 10  # Обернений середній час

# Генеруємо дані для випадкових часів між дефектами
x = np.linspace(0, 50, 1000)
y = lmbda * np.exp(-lmbda * x)

# Побудова графіка
plt.plot(x, y, label='Експоненційний розподіл')
plt.title('Експоненційний розподіл часу між дефектами')
plt.xlabel('Час між дефектами (години)')
plt.ylabel('Щільність ймовірності')
plt.legend()
plt.show()


#%%

import random
        
def G():  
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)
    
    
print(G())









