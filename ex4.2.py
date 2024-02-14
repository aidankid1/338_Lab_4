import timeit
import random
from matplotlib import pyplot as plt

# 3) Inefficient search for sorted array (linear search)
def inefficientSearch (array, key):
    for i in range(len(array)):
        for j in range(len(array)):
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
NUMBER_OF_TIMES = 10

randList = [x for x in range(INPUT_SIZE)]   #Makes a list of 1000 elements

avg_efficient = []
avg_inefficient = []
for i in range(NUMBER_OF_TIMES):
    target = randList[random.randint(0, INPUT_SIZE - 1)]   #Minus one to ensure the random number is guaranteed to be in the list
    inefficientTime = timeit.timeit(lambda: inefficientSearch(randList, target), number=ITERATIONS)
    avg_inefficient.append(inefficientTime)

    efficientTime = timeit.timeit(lambda: efficientSearch(randList, 0, len(randList) - 1, target), number=ITERATIONS)
    avg_efficient.append(efficientTime)

for x in range(NUMBER_OF_TIMES):
    avg_efficient[x] /= NUMBER_OF_TIMES
    avg_inefficient[x] /= NUMBER_OF_TIMES

testRunNumber = [k + 1 for k in range(NUMBER_OF_TIMES)]

plt.scatter(testRunNumber, avg_efficient, label='Binary Search')
plt.scatter(testRunNumber, avg_inefficient, label='Linear Search')
plt.xlabel('Test Number')
plt.ylabel('Average Time (s)')
plt.legend()
plt.show()