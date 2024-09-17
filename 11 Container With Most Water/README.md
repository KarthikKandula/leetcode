# 11. Container With Most Water

1 possible solution for this problem  

## Method 1

Use two pointers to solve the problem.

```
"""
    Use two pointers to solve the problem

    Loop thru the input array by checking the current capacity for that loop
        current capacity is min of current heights * the distance between those heights
        replace output maxCap is current capacity is higher
    
    Keep pointers moving based on the lowest value
        additional condition to move left is values are equal
"""
```
