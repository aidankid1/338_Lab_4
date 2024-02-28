1:
There are various factors which affect the execution time of a program. To minimize the effects of this we can use timeit and repeat. Using timeit aims to deal with noise by using a single time measurement when executing the code. It is useful to obtain an average execution time and can help compare how different approaches perform. Using repeat 

2:
The appropriate statistic to apply to the output of timeit.timeit() is the average because timeit results in a single measurement for the time of all executions so it would tell you the overall performance if you took the average. The appropriate statistic to apply to the output of timeit.repeat() is min and max because it will give you a range. The range is the worst case to best case, which would give you a better understanding of its performance for different runs.
