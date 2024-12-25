# 26. Remove Duplicates from Sorted Array

1 possible solution for this problem  

### Self Notes


```
"""
    Other solution -- same time & space

    this is same as my solution but with different code & slightly tweaked approach
        this approach always keeps track of the location to update next with left pointer
        the comparisions are made with right pointer & right - 1
            since there will be duplicates, this comparision also works to find unique values
        once a unique value has been found, replace it with left pointer location
            increment left pointer location
"""

"""
    Own solution

    this solution always keeps track of the last unique value with the left pointer
        always compares the last unique pointer with right pointer
        once a new value is found
            we increment the left pointer first, to update the next variable
            and then update the value
"""
```

