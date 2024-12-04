# 50. Pow(x, n)

1 possible solution for this problem  

### Self Notes


```
"""
    NeetCode Optimal solution

    the advantage with dealing with power operations is 
        2^32 = 2^16 * 2^16
        so if we calculate 2^16 value once, we can multiply it with itself to get 2^32 value
        we use this to our advantage essentially reducing the no. of operations 
        so time complexity if O(log n)
"""
```

