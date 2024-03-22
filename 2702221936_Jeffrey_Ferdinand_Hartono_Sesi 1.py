# -*- coding: utf-8 -*-
"""2702221936-Jeffrey Ferdinand Hartono-LAB01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZAvBtdVBBFzs2P2qbwcvJuYmZmqrM1SO
"""

import time
print(time.ctime())

x = 1
x

x = x + 1
x

x = 1
y = x + 1
x = 2
y

import numpy as np
x = np.array([1,4,3])
x

y = np.array([[1,4,3],[2,9,7]])
y

def my_adder(a,b,c):
    """
    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author:
    date:
    """

    # this is the summation
    out = a + b + c

    return out

my_adder(1,2,3)

help(my_adder)

def my_thermo_stat(temp, desired_temp):
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status

status = my_thermo_stat(65,75)
print(status)

status = my_thermo_stat(75,65)
print(status)

status = my_thermo_stat(65,63)
print(status)

x = 3
if x > 1 and x < 2:
    y = 2
elif x > 2 and x < 4:
    y = 4
else:
    y = 0
print(y)

x = 3
if 1 < x < 2:
    y = 2
elif 2 < x < 4:
    y = 4
else:
    y = 0
print(y)