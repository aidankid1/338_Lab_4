1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) [0.1 pts]
There are several advantages and disadvantages to using either arrays or linked lists. Arrays can be advantageous because they allow direct indexing which allows for O(1) time complexity when trying to access elements. Contiguous memory allocation allows for efficient memory. In comparison linked lists are at a disadvantage as they are not easily indexable and require more memory as they need to store the pointers. Linked lists are advantageous because they are dynamic so they don’t need to be resized and they allow easy insertion and deletion (O(1)). In comparison the size of an array is fixed and would need to be resized. Inserting and deleting elements of an array is not as simple and has a time complexity of O(n). 

2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? [0.1 pts]

This function can be implemented to minimize the impact of each standalone task by determining the index of the element needing to be replaced using a method for deleting and then a separate method for inserting into that space. Perform the deletion then the insertion to minimize the impact of the tasks.

3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why it is possible or not to use them. [0.4 pts]
Insertion sort
If we are implementing a doubly linked list it is feasible to use insertion sort. It is possible to use this function because insertion sort will create the sorted list by iterating through the elements and inserting the elements into their proper position one at a time. 
Merge sort
If we are implementing a doubly linked list it is feasible to use merge sort. It is possible to use this function because it is a divide and conquer algorithm so it can split the list into sublists, then sort by traversing through the sublist, and then combine sorted sublists back together. 

4. Also show the expected complexity for each and how it differs from applying it to a regular array [0.4 pts]

Insertion:
Regular Array: Best: O(n), Average: O(n^2), Worst: O(n^2)
Doubly Linked List: O(n), Average: O(n^2), Worst: O(n^2)

Insertion sort would differ from an array because in an array direct indexing is used to sort but in a doubly linked list rearranging the pointers is needed. Traversing through the list to insert is needed for the list whereas in an array you can just swap because of direct indexing. 

Merge:
Regular Array: O(nlogn)
Doubly Linked List: O(nlogn)

Merge sort would split both the array and list in half recursively and then iterate through to sort. Compared to a regular array there isn’t that big of a difference. 
