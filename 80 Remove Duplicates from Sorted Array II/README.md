# 80. Remove Duplicates from Sorted Array II

1 possible solution for this problem  

### Self Notes


```
"""
    can solve this problem using two pointers with a twist
        the idea is to know how many times a value appears in the input
            looping thru that many times to place the value in left pointers location
    
    take two pointers left & right at the beginning
    loop while right pointer is less than length of input
        get count of the current value right is pointing at
            initialize a variable count with value 1, since every value appears atleast once
            loop while right value is same as next value
                increment count
        by the above loops end, we get count of the current right pointer value
            and right is pointing at the end of that value
        loop again for the min of (2, count)
            to make sure 1's are accounted & loop is not more than twice
            place right pointers value (pointing to the last occurence of current value) in left pointers location
            increment left pointer
        by the end of above loop, current value is taken care of
        increment right pointer value to point at the next unique value
"""
```

