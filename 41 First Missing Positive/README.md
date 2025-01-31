# 41. First Missing Positive

1 possible solution for this problem  


```
"""
    this problem can be implemented using cyclic sort algorithm
        cyclic sort is used to sort values in an array
        we use cyclic sort to place values in their respective places
        go thru the array again to find the first value that isn't in place
            so that index value is the smallest positive integer that isn't present in nums
        
    the intuition is as below
        we need to find the smallest +ve integer not in nums
        so possible values in nums are from 1...n
            we only need to check these values
        due to the way indexes work in programming
            for each index -- value should be index + 1
            for each value -- it should be in index value - 1
        so after implementing cyclic sort, all values need to be in their places aka above logic
            the first index that violates this logic, is the missing nubmer
"""
```

