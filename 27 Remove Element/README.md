# 88. Merge Sorted Array

1 possible solution for this problem  

### Self Notes


```
"""
    solve this problem using a single-pass two-pointer approach
        the goal is to remove all occurrences of a given value from the array
        use one pointer to iterate through the array
            this pointer checks each element
        use another pointer to track the position where the next valid (non-val) element should go
            this ensures all valid elements are shifted to the front of the array
        for each element, if it is not equal to the target value:
            copy it to the position of the second pointer
            increment the second pointer
        return the value of the second pointer, which indicates the length of the array without the target value
"""
```

