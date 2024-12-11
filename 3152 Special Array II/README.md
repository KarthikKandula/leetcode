# 3152. Special Array II

1 possible solution for this problem  

### Self Notes


```
"""
    the idea is to make the solution faster by 
        precalculating the mismatches until that point from start by checking
            if there are any odd & even's side by side
            increment that index's value by 1
            also carry on the value for each index & add 1 if there is a mismatch at that location
        
        while comparing from the queries
            the difference of from & to values from count array should be 0
                it indicates there are no adjacent odd & even values
            if diff is not 0, append False to result array
"""
```

