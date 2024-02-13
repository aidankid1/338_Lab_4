# 1) The worst case complexity for this code is O(n^2). The best case is O(n). Lastly, the average case is the same as the worst case
#    which is O(n^2). The reason the worst case is O(n^2) is cause if every element is greater than 5, it would have to go through 
#    the whole list again. This means for every existing element, you would have to go through the list 'n' times. Assuming the list
#    has 'n' elements where for each element you have to go through 'n' times, it would become O(n^2). The average case is n^2 / 2 but
#    because constant values have little affect on the time complexity in the long run, it would average out to n^2. Lastly, the best case
#    is O(n) because if no values are greater than 5, it would only have to go through the list one time and would not have to update the list
#    at all.


# 2) No, the worst, average and best cases aren't the same. Below is a modified version that makes the worst, average and best case the same
#    complexity. It will multiply each element in the list 'n' times without any conditions, making it O(n^2) for worst, average and best case.
def processdata(li):
    for i in range(len(li)):
        for _ in range(len(li)):
            li[i] *= 2
