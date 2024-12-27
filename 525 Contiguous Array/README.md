# 525. Contiguous Array

1 possible solution for this problem  

### Self Notes


```
"""
    we can solve this problem using prefix sum
        subtract 1 from prefix sum for every 0 value
        add 1 to prefix sum for every 1 value
        the idea is a prefix sum value appears again in the array
            it means between the last location & the new location there are same num of 0 & 1 
            get the max value of existing output value & the new window
        if at any point prefix sum becomes 0
            update the max value with current index 
            since only happens if there are same num of 0 & 1
"""
```

