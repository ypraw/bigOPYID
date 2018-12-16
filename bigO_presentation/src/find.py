import time
from random import randrange
import matplotlib.pyplot as plt
import numpy as np


# O(N)
def findmin1(data):
    lowest = data[0]
    for i in data:
        if i < lowest:  # di eksekusi selama n
            lowest = i  # dieksekusi 1 kali
    return lowest  #   dieksekusi 1 kali


# O(N^2)
def findmin2(data):
    lowest = data[0]
    for i in data:  # N
        isSmallest = True
        for j in data:  # N
            if i > j:
                isSmallest = False
            if isSmallest:
                lowest = i
    return lowest


def findmin3(data):
    return min(data)


#example_list=[5,3,6,4,1]
plt.xlabel("size")
plt.ylabel("time")
#print(findmin1(example_list))
#print(findmin2(example_list))
x1 = []
y1 = []
for listSize1 in range(1000, 10001, 1000):
    example_list = [randrange(10000) for x in range(listSize1)]
    start_time = time.time()
    print(f'minimum value: {findmin1(example_list)}')
    end_time = time.time()
    et = end_time - start_time
    print(f'size list: {listSize1}, time execution: {et:5f}')
    x1.append(listSize1)
    y1.append(et)
print()

x2 = []
y2 = []
for listSize2 in range(1000, 10001, 1000):
    example_list = [randrange(100000) for x in range(listSize2)]
    start_time = time.time()
    print(f'minimum value: {findmin2(example_list)}')
    end_time = time.time()
    et2 = end_time - start_time
    print(f'size list: {listSize2}, time execution: {et2:.5f}')
    x2.append(listSize2)
    y2.append(et2)
print()

x3 = []
y3 = []
for listSize3 in range(1000, 10001, 1000):
    example_list3 = [randrange(100000) for x in range(listSize3)]
    start_time = time.time()
    print(f'minimum value: {findmin3(example_list3)}')
    end_time = time.time()
    et3 = end_time - start_time
    print(f'size list: {listSize3}, time execution: {et3:.5f}')
    x3.append(listSize3)
    y3.append(et3)
print()
tx = y1[5:] + y2[:5]
plt.plot(x1, tx, 'g-', alpha=1)
plt.plot(x2, tx, 'r-', alpha=1)
# Label the axes and provide a title
plt.title("haha")
plt.grid(True)
plt.xlabel("size")
plt.ylabel("time")
plt.show()