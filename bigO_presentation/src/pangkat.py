import timeit
from math import pow


# O(N)
def pangkat1(x, y):
    hasil = 1
    for i in range(0, y):
        hasil = x * hasil
    return hasil


# O(N)
def pangkat2(x, y):
    # hasil = x**y
    return x**y


# O(1)
def pangkat3(x, y):
    # hasil = pow(x, y)
    return pow(x, y)


""" Testing"""
#print(pangkat1(100000,100000))
print(
    f'with loop \t {timeit.timeit("pangkat1(100,100)",globals=globals(),number=100000):5f}'
)
print(
    f'with ** operator {timeit.timeit("pangkat2(100,100)",globals=globals(),number=100000):5f}'
)
print(
    f'with pow \t {timeit.timeit("pangkat3(100,100)",globals=globals(),number=100000):5f}'
)
#print(timeit.timeit("math.pow(100,100)",globals=globals(),number=1000, setup="import math"))
