import timeit
from random import randrange
from collections import OrderedDict
import numpy as np


def listCompre(sizeList):
    result = [x for x in range(sizeList)]
    return result


def numpyList(sizeList):
    myList = np.arange(sizeList)
    return myList


def insertList(sizeList):
    i = 0
    mylist = []
    while i <= sizeList:
        mylist.insert(len(mylist), i)
        i += 1
    return mylist


def appendList(sizeList):
    i = 0
    mylist = []
    while i <= sizeList:
        mylist.append(i)
        i += 1
    return mylist


""" Testing"""
item = 100000
number = 100

exeTimeAppend = timeit.timeit(
    "appendList(item)", number=number, globals=globals())
exeTimeInsert = timeit.timeit(
    "insertList(item)", number=number, globals=globals())
exeTimeNumpy = timeit.timeit(
    "numpyList(item)", number=number, globals=globals())
exeTimeCompre = timeit.timeit(
    "listCompre(item)", number=number, globals=globals())

result = dict(
    insertList=exeTimeInsert,
    appendList=exeTimeAppend,
    numpyList=exeTimeNumpy,
    compreList=exeTimeCompre)
result = OrderedDict(sorted(result.items(), key=lambda x: x[1]))
for k, v in result.items():
    print(f'{k} : {v:.5f} seconds')
