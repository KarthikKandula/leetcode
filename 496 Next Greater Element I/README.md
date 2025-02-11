# 496. Next Greater Element I

1 possible solution for this problem  


```
"""
    a bit better optimized solution

    we can bypass using multiple array altogether by using hashmap for storing answers 
        rather than use extra memory for the arrays
        if a value doesn't exist in the hashmap, it means there's no greater element for that number
"""

"""
    My solution

    we can use monotonic stack and hashmap to solve the problem
        use hashmap to track indexes from nums1
            populate hashmap with values & their indexes from nums1
        loop thru nums2 to populate ans2 to find next greater element for each element
            update index in hashmap to match to nums2 indexes
        loop thru nums1 again to populate correct values into ans array
            fetching from indexes from hashmap
"""
```

