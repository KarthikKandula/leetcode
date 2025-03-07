# 1011. Capacity To Ship Packages Within D Days

1 possible solution for this problem  


```
"""
    This is a classic binary search problem
        if we look at the problem statement a bit
            we realize that there exists a min capacity, i.e the max value in the array
            so if there exists a max value, it is a binary search problem
                the max value is the sum of all weights in the input
        if we loop between the min & max value 
            check for a right fit, the least value that satisfies this condition is the answer
        to see if we can satisfy for a certain capacity value
            go in order & add to a temp value
                if at any time, the temp value is greater than capacity
                    reset capacity value
                    increment days needed value
                done until end, we'll know how many days this capacity needs
        the lowest capacity at which all weights can be carried is the answer
"""
```

