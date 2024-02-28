import timeit
import random 
from matplotlib import pyplot as plt
import numpy as np
import scipy

# 1) Linked List Node Class
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
        
def newNode(x):
    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp

# 2) Function to find Middle element For Binary Search
def middle(start, last):
    if (start == None):
        return None
    slow = start
    fast = start.next
    while (fast != last):
        fast = fast.next
        if (fast != last):
            slow = slow.next
            fast = fast.next
    return slow

# Binary Search Function On linked list
def binarySearchList(head, value):
    start = head
    last = None
    while True:
        mid = middle(start, last) # Find middle
        if (mid == None): # If middle is empty
            return None
        if (mid.data == value): # If value is present at middle
            return mid
        elif (mid.data < value): # If value is more than mid
            start = mid.next
        else: # If the value is less than mid.
            last = mid
        if not (last == None or last != start):
            break
    return None #Value Not Found

# 3) Array Class used to store integers
class Array:
    #Constructor
    def __init__(self, arr):
        self.arr = arr
    
    #Gets value at index
    def getValue(self, index):
        return self.arr[index]
    
    #Gets length of array
    def getLength(self):
        return len(self.arr)
    
#Binary Search for Array
def binarySearchArray (arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2
        if(key == arr.getValue(mid)):
            return mid
        elif(key < arr.getValue(mid)):
            return binarySearchArray(arr, first, mid - 1, key)
        elif(key > arr.getValue(mid)):
            return binarySearchArray(arr, mid + 1, last, key)
    return -1 #Key was not found in the array

#Makes a singly linked list of integers of the required size and returns the fully linked list
def populateList(SIZE):
    current = newNode(0)
    head = current

    for i in range(SIZE):
        current.next = newNode(i + 1)
        current = current.next

    return head

#Function for fitting logarithmic data curve fitting
def func(x, a, b):
    return a * np.log2(x) + b

# 4) The complexity of binary search on linked list is O(n) due to the fact that there is no way of
#    indexing each node for the linked list. This means we must traverse the whole list in order to find the middle element
#    for a linked list. For that reason, in order to perform binary search on 
#    a linked list, the worst case is for you to traverse through the list of 'n' nodes in 
#    order to find the nth element; in our case, its to find the middle element. 

# 5)
INPUT_SIZE = [1000, 2000, 4000, 8000]   #Number of elements for array and linked list
ITERATIONS = 100    #Number of Iterations

#List for average times calculated for each input size
avgLinkedList = []
avgArray = []

for size in INPUT_SIZE:
    #Uses class Array to store integers
    randArray = Array([i for i in range(0, size)])
    head = populateList(size)

    #To ensure it is randomized the best it can, the key is randomized for each iteration of our test
    linkedListBinary = timeit.repeat(lambda: binarySearchList(head, randArray.getValue(random.randint(0, size - 1))), repeat=ITERATIONS, number=1)
    arrayBinary = timeit.repeat(lambda: binarySearchArray(randArray, 0, randArray.getLength() - 1, randArray.getValue(random.randint(0, size - 1))), repeat=ITERATIONS, number=1)

    #Sum up the times for each input size and divides it by the # of times it was ran
    avgLinkedList.append(sum(linkedListBinary) / ITERATIONS)
    avgArray.append(sum(arrayBinary) / ITERATIONS)

#6)
# Plotting and curve fitting average time for Arrays
popt, pcov = scipy.optimize.curve_fit(func, INPUT_SIZE, avgArray)
plt.scatter(INPUT_SIZE, avgArray, label='Array')
x_values = np.linspace(min(INPUT_SIZE), max(INPUT_SIZE), 100)
fitted_curve = func(x_values, *popt)
plt.plot(x_values, fitted_curve, 'b')

# Plotting and curve fitting average time for Linked Lists
slope, intercept = np.polyfit(INPUT_SIZE, avgLinkedList, 1)
plt.scatter(INPUT_SIZE, avgLinkedList, label='Linked List')
linevalues = [slope * x + intercept for x in INPUT_SIZE]
plt.plot(INPUT_SIZE, linevalues, 'r')

plt.title(label='Performing Binary Search on Varying Input Sizes For Linked List VS Array')
plt.xlabel('Input Size')
plt.ylabel('Average Time (s)')
plt.legend(loc='upper left')
plt.show()