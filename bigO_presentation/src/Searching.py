import timeit
import time
import matplotlib.pyplot as plt
import numpy as np


# Find target 22 (i.e. return its index)in a sorted list
# Here we use Binary Search algorithm because its time complexity is O(log n)
def binarySearch(lst, search):
    lower_bound = 0
    upper_bound = len(lst) - 1
    while True:
        if upper_bound < lower_bound:
            print("Not found.")
            return -1

        i = (lower_bound + upper_bound) // 2

        if lst[i] < search:
            lower_bound = i + 1
        elif lst[i] > search:
            upper_bound = i - 1
        else:
            # return [search, i]
            print(f"Element {search} ditemukan di indeks {i}")
            return 0


print(f"binary search : {binarySearch([1, 3, 9, 22], 2)}")

# print(
#     f'element {binarySearch([1, 3, 9, 22], 22)[0]} ditemukan pada indeks ke {binarySearch([1, 3, 9, 22], 22)[1]} ',
# )


# Find target 22 (i.e. return its index)in a sorted list
def linearSearch(sortedList, target):
    for i in range(len(sortedList)):
        if (sortedList[i] == target):
            return [i, sortedList[i]]
    return -1


print(
    f'element {linearSearch([1, 3, 9, 22], 22)[0]} ditemukan pada indeks ke {linearSearch([1, 3, 9, 22], 22)[1]} ',
)
#exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(sumoflistLogN(exampleList))

# """ Testing Runtime """
# size1, size2, time1, time2 = [], [], [], []

# for listSize in range(1000, 10001, 1000):
#     exampleList = [x for x in range(listSize)]
#     start_time = time.time()
#     print(
#         f"binary search O(log N) : {binarySearch(exampleList,exampleList[len(exampleList)-1])}"
#     )
#     end_time = time.time()
#     et = end_time - start_time
#     print(f'size list: {listSize}, time execution: {et:.5f}')
#     size1.append(listSize)
#     time1.append(et)

# print(" ")

# for listSize2 in range(1000, 10001, 1000):
#     exampleList2 = [x for x in range(listSize2)]
#     start_time2 = time.time()
#     print(
#         f"sum of list with linier bigO : {linearSearch(exampleList2,exampleList2[len(exampleList2)-1])}"
#     )
#     end_time2 = time.time()
#     et2 = end_time2 - start_time2
#     print(f'size list: {listSize2}, time execution: {et2:.5f}')
#     size2.append(listSize2)
#     time2.append(et2)

# plt.plot(size1, time1, 'g-', alpha=1, label="Binary Search")
# plt.grid(True)

# plt.plot(size2, time2, 'r-', alpha=1, label="Linear Search")
# # Label the axes and provide a title
# plt.title("haha")
# plt.legend()
# plt.show()