# 217. Contains Duplicate

I can think of 3 possible solutions for this problem

## Method 1

Use Set & compare length of input to the length of set

```
"""
    Use set
        Set returns unique values for an input

    if length of input != length of set, return True, else False
"""
```

## Method 2

Use an array to record unique values, compare the values with next value from input, if found in unique array, return true.  
If loop reached end, return false

```
""" -->'Time Limit Exceeded'<--
    Create an array to take note of unique values in nums
    for each value in nums
        if value already exists in unique -> duplicate value, return True
        if doesn't exist -> append to unique

    if full nums in traversed -> it means values are unique
"""
```


## Method 3

Sort & compare two adjacent elements  
