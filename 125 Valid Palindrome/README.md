# 125. Valid Palindrome

1 possible solution for this problem

## Method 1

Since the problem statement asks us to check for palindrome, we have to check the same location from front as well as the back, to do this efficiently use ***two pointers*** to solve this problem.  

```
"""
    Use two pointers

    Use two pointers to access two ends of the input string
        check if the value at a place is alphanumeric (use is alnum), skip if it is - do for both left & right pointer
        else compare the values
            if doesn't match -> return false (palindrome should have same values)
            if matches, proceed to next location
"""
```
