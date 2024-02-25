import timeit
import random 
from matplotlib import pyplot as plt
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

# 3) 
class Array:
    #Creates an array of length n with zeros
    def __init__(self, size):
        self.size = size
        self.data = [0]*size

    #For setting the values of an array using the index with the integer to put in
    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

#Binary Search for Arrays O(log(n))
def binarySearchArray (arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2
        if(key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            return binarySearchArray(arr, first, mid - 1, key)
        elif(key > arr[mid]):
            return binarySearchArray(arr, mid + 1, last, key)
    return -1 #Key was not found in the array

# 4) The complexity of binary search on linked list is O(n) due to the fact that there is no way of
#    indexing each node for the linked list. For that reason, in order to perform binary search on 
#    a linked list, the worst case is for you to traverse through the list of 'n' nodes in 
#    order to find the nth element. 

# 5)
INPUT_SIZE = [1000, 2000, 4000, 8000]   #Number of elements for array and linked list
ITERATIONS = 100    #Number of Iterations

for size in INPUT_SIZE:
    print("HIU")
    # linkedListBinary = timeit.repeat(lambda: LINKEDLIST(), repeat=ITERATIONS, number=1)
    # arrayBinary = timeit.repeat(lambda: LINKEDLIST(), repeat=ITERATIONS, number=1)

# popt, pcov = scipy.optimize.curve_fit(func, SIZE_LIST, avg_insertion_list)
# popt2, pcov2 = scipy.optimize.curve_fit(func, SIZE_LIST, avg_binary_insertion)

# plt.scatter(INPUT_SIZE, avg_linear, label='Linked List')
# plt.scatter(INPUT_SIZE, avg_quick_binary, label='Array')

# # Plot the fitted curve
# x_values = np.linspace(min(SIZE_LIST), max(SIZE_LIST), 100)
# fitted_curve = func(x_values, *popt)
# fitted_curve2 = func(x_values, *popt2)
    
# Plotting the data and the fitted curve
# plt.plot(x_values, fitted_curve, 'b')
# plt.plot(x_values, fitted_curve2, 'r')

# plt.title(label='Average Timing With Binary Search on Varying Input Sizes For Linked List VS Array')
# plt.xlabel('Input Sizes')
# plt.ylabel('Average Time (s)')
# plt.legend(loc='upper right')
# plt.show()