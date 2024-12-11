# 2779. Maximum Beauty of an Array After Applying Operation

1 possible solution for this problem  

### Self Notes


```
"""
    the idea here to find the largest window within the array that satisfies the condition
        largest num - small num <= k * 2
            this is a mathematical formula that should satisfy for this problem
        sort the array so that
        sorting the array to simplify the problem
            after sorting, the difference between the largest and smallest numbers is simply - nums[r]−nums[l]

        so we start the problem with window starting at l, r
        as we move higher in the window, calculate if the condition is holding up
            if condition is broken, increment left pointer
        
        in the end, the length of the array where the condition holds up is the answer
            hence return r - l + 1, this is the window length
"""
```

