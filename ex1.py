import timeit
import random 
from matplotlib import pyplot as plt
import numpy as np
# Link list node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
        
class Array:
    def __init__(self, data):
        return
    # IDK LMFAO

def newNode(x):
    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp
# function to find out middle element
def middle(start, last):

    if (start == None):
        return None

    slow = start
    fast = start . next

    while (fast != last):
    
        fast = fast . next
        if (fast != last):
        
            slow = slow . next
            fast = fast . next
        
    return slow

def binary_search(head, num):

    start = head
    last = None

    while True :
    
        # Find middle
        mid = middle(start, last)

        # If middle is empty
        if (mid == None):
            return None

        # If value is present at middle
        if (mid . data == num):
            return mid

        # If value is more than mid
        elif (mid . data < num):
            start = mid . next

        # If the value is less than mid.
        else:
            last = mid

        if not (last == None or last != start):
            break

    # value not present
    return None

# 4)

# 5)
INPUT_SIZE = [1000, 2000, 4000, 8000]   #Number of eleements for array and or linked list
ITERATIONS = 100    #Number of Iterations

for size in INPUT_SIZE:
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