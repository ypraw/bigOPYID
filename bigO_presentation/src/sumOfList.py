import timeit


# O(log n)
def SumOfList(MyList):
    if len(MyList) == 1:  #cost = a
        return MyList[0]  #cost = b
    mid = len(MyList) // 2  #cost = c
    left = SumOfList(MyList[:mid])  #cost = f(n/2) + h
    right = SumOfList(MyList[mid:])  #cost = f(n/2) + i
    return left + right  #cost = d


# O(N)
def SumOfList2(myList):
    total = 0
    for index in range(0, len(myList)):
        total += myList[index]
    return total


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
""" print(SumOfList(data))
print(SumOfList2(data)) """

number = 10000

timerSumLinier = timeit.timeit(
    "SumOfList(data)", globals=globals(), number=number)
timerSumLogarithmic = timeit.timeit(
    "SumOfList2(data)", globals=globals(), number=number)

print(
    f"Time for Linier:\t{timerSumLinier}\nTime for Logarithmic:\t{timerSumLogarithmic}"
)
