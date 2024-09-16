# 15. 3Sum

1 possible solution for this problem  

## Method 1

If you divide this problem into sub-problems, a part of it is similar to two sum II.  
We can use two sum II's solution with a slight twist to get to solution. Similar to two sum II, it would help to sort the array. Iterate thru each value (outer loop) & implement two sum II (inner loop). Introduce code to handle duplicate values as asked in the problem statement.  

```
"""
    If you divide the problems into sub-problems, it's similar to two sum II

    A sorted array helps to solve easily
    Use two pointers inside an outer loop that iterates thru numbers in a order
        introduce code to handle for duplicates
"""
```
