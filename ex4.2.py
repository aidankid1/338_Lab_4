import timeit
import random
from matplotlib import pyplot as plt

# 3)
def inefficientSearch (array, key):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == key:
                return i
    return -1 #If key is not found

def efficientSearch (array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1 #If key is not found

#4) The worst case for inefficentSearch is O(n^2) as it compares the same values 'n' times for 'n' elements.
#   The worst case for efficientSearch is O(n) as it must go through the whole list one time for 'n' elements.

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

    efficientTime = timeit.timeit(lambda: efficientSearch(randList, target), number=ITERATIONS)
    avg_efficient.append(efficientTime)

for x in range(NUMBER_OF_TIMES):
    avg_efficient[x] /= NUMBER_OF_TIMES
    avg_inefficient[x] /= NUMBER_OF_TIMES

lol = [k + 1 for k in range(NUMBER_OF_TIMES)]

plt.scatter(lol, avg_efficient, label='Efficient')
plt.scatter(lol, avg_inefficient, label='Inefficient')
plt.xlabel('Test Number')
plt.ylabel('Average Time (s)')
plt.legend()
plt.show()