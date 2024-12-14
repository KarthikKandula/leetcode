# 2593. Find Score of an Array After Marking All Elements

1 possible solution for this problem  

### Self Notes


```
"""
    solve this problem using minHeap & set
        minHeap is useful to always get the lowest value from the remaining values
        the idea is to use the set to record marked indexes

    insert all values in nums to the heap in format -- [value, index]

    loop while minHeap has values
        get rid of all the values in minHeap whose indexes are already in set
            after this operation, the lowest value in heap is unmarked
        
        get the lowest value from heap
            add value to score variable
            add it's index along with adjacent indexes to set

    in the end return score value
"""
```

