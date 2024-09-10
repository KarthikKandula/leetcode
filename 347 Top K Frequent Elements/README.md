# 347. Top K Frequent Elements

3 possible solutions for this problem

## Method 1

Use a hashmap to count elements
Use a count array (of size len(nums)+1), to keep record the amount of time elements repeat via indexes
Iterate thru the count array in desc order, append to new result array, if length is as k, return result array 

```
"""
    NeetCode solution - o(n)

        Use a hashmap to count elements
        Use a count array (of size len(nums)+1), to keep record the amount of time elements repeat via indexes
        Iterate thru the count array in desc order, append to new result array, if length is as k, return result array 
"""
```

## Method 2 (Using heap)

Use a hashmap to count elements
For all elements in hashmap, insert into heap in a way as (-count, value)
    -count since python implements minheap, so -ve'ing it makes it max heap
now, pop from heap k times

```
"""
    Another solution (using heap)

        Use a hashmap to count elements
        For all elements in hashmap, insert into heap in a way as (-count, value)
            -count since python implements minheap, so -ve'ing it makes it max heap
        now, pop from heap k times
"""
```

## Method 3 (My Solution)

Use a hashmap to record no. of times each value occurs  
Sort the hashmap's values in descending order  
get the k elements from sorted values & extract from hashmap those elements, put them in an array & return

