#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:44:10 2023

@author: prestige
"""

import random
# random.seed(0)
# print(random.randint(1, 5))
# print(random.choice(['apple', 'banana', 'cat']))

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    random_number = random.randint(0, 98)
    
    if random_number % 2 != 0:
        random_number += 1
    
    return random_number

# print(genEven())

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    random_number = random.randint(9, 20)
    if random_number % 2 != 0:
        random_number += 1
    
    return random_number

# print(deterministicNumber())

# print(int(random.random() * 10))

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 
    
    
# print(dist1())
# print(dist2())


'''
1-1
1-2
1-3
1-4
2-1
2-2
2-3
2-4
3-1
3-2
3-3
3-4
4-1
4-2
4-3
4-4


1/16 + 2/16 

0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

1/52 * 1/51

4/52 * 3/51


3/6 * 2/5 * 1/4 = 6/120 = 1/20
3/6 * 3/5 * 2*4 = 1/2 * 3/5 * 1/2 = 3/20

1/8

'''

    
    