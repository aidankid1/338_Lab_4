
#1:
#The strategy for growth is to have mild amounts of overallocation, just enough to give linear time amortization
#over a long sequence of appends. As well as always being a multiple of 4. It follows the sequence 
#0,4,8,16,24,32,40,52,64,76 as described on lines 60-68 in the lists.c file.
#5:
#It takes slightly longer to increase the array size from S to S+1 then it does to increase it from S-1 to S.
#this makes sense as increasing to S+1 requires the copying of 12 additional elements and additionally it is 
#more likely that the array will have to be moved to a new pace in memory.
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