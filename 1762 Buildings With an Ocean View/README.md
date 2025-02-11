# 1762. Buildings With an Ocean View

1 possible solution for this problem  


```
"""
    O(1) space approach

    instead of using stack, we can implement this using constant space
        we need to find the buildings that have a view
        i.e., all the buildings that don't have a higher building after it
        if we traverse the array in reverse order
            only max values & values that beat this max value has a view
            we can eliminate the array & use a single variable to record the max value 
            if a higher value is found, insert that value into the result array
"""

"""
    Monotonic Stack approach

    this is similar to any monotonic stack
        looking carefully at the problem we realize this is a monotonic increasing stack problem
        but in the end, we return values in the stack
"""
```

