import timeit
import random
from matplotlib import pyplot as plt

# 3) Inefficient search for sorted array (linear search)
def inefficientSearch (array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1 #If key is not found

# Efficient Search for sorted array (binary search)
def efficientSearch (array, first, last, key):
    while first <= last:
        mid = (first + last) // 2
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1  # Key was not found in the array

#4) The worst case for inefficentSearch is O(n) as it goes through the whole list one time for 'n' elements
#   The worst case for efficientSearch is O(nlog(n)) as it must go through the whole list halved each time.

#5) 
INPUT_SIZE = 1000
ITERATIONS = 100

avg_efficient = []
avg_inefficient = []
for i in range(ITERATIONS):
    randList = [random.randint(0, INPUT_SIZE) for _ in range(INPUT_SIZE)]
    randList.sort()
    target = random.choice(randList)   
    avg_inefficient.append(timeit.timeit(lambda: inefficientSearch(randList, target), number=1))
    avg_efficient.append(timeit.timeit(lambda: efficientSearch(randList, 0, len(randList) - 1, target), number=1))

plt.xlabel('Average Time (s)')
plt.ylabel('Frequency')
plt.hist(avg_efficient, bins=10, alpha=0.5, label='Binary Search')
plt.hist(avg_inefficient, bins=10, alpha=0.4, label='Linear Search')
plt.legend()
plt.show()