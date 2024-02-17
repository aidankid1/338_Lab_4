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
INPUT_SIZE = [1000, 2000, 4000, 8000]