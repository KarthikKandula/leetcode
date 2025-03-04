# 986. Interval List Intersections

1 possible solution for this problem  


```
"""
    This solution uses merge intervals logic a bit
        we need to find overlapping intervals
        so we use two pointers in each input & traverse thru each input
            comparing the values from both lists to each other
        get the max value of min values & min value of max values for each comparision
            only insert into result if they're valid aka l <= r
        keep moving either i or j pointer based on
            if i max value is less -- move i pointer
            if j max value is less -- move j pointer
"""
```

