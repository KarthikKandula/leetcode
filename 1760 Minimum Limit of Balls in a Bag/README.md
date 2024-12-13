# 1760. Minimum Limit of Balls in a Bag

1 possible solution for this problem  

### Self Notes


```
"""
    the idea is to 
        check for each possible value if it's possible to divide all values in input nums
        the lowest value that it's possible to divide is the result

        to achieve this, we take the max number in nums & try to check for each number from 1...maxval
        an efficient way to do this is to use binary search, so we halve the no. of checks
"""
```

