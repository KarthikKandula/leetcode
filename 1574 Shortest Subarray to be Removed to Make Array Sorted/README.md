# 1574. Shortest Subarray to be Removed to Make Array Sorted

1 possible solution for this problem  


```
"""
    we can solve the problem using classic two pointer method with couple twists
        the jist of this problem is figuring out the middle portion of the array to remove
        to get that, we need to find increasing values starting with first element
            also find increasing value ending with last element
        now, once the increasing values have been found with the last element
            start from the first element and increase left pointer one by one as long as
                the left pointer is less than right pointer
                update mid subarray length (res variable) in each loop -- get min value
            if at any point, left value is greater, increment right pointer
            keep doing it until the end and the min subarray length is in the result variable
        this method works since, we're considering all possiblities
"""
```

