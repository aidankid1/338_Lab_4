import sys
import timeit
from matplotlib import pyplot as plt
testList = []
currentCapacity = sys.getsizeof(testList)
print("The capacity of the array before enetering the loop is",currentCapacity," bytes")
#loop will append an element to test list each run and print a statement when the capacity increases
for x in range(64):
    testList.append(x)
    newCapacity = sys.getsizeof(testList)
    if newCapacity > currentCapacity:
        print("when the ",x+1,"th element is appended the capacity increased from ",currentCapacity," to ",newCapacity)
        currentCapacity = newCapacity
def growArray(a):
    a.append(1)
growStoS1 = []
growS1toS = []
for x in range(1000):
    testlist = [y for y in range(64)]
    growStoS1.append(timeit.timeit(lambda: growArray(testlist), number = 1))
    testlist = [y for y in range(52)]
    growS1toS.append(timeit.timeit(lambda: growArray(testlist), number = 1))
plt.hist(growStoS1)
plt.savefig("ex3StoS1.jpg")
plt.clf()
plt.hist(growS1toS)
plt.savefig("ex3S1toS.jpg")
plt.clf()