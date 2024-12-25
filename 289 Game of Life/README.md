# 289. Game of Life

1 possible solution for this problem  

### Self Notes


```
"""
    we can solve this problem using dfs matrix traversal
        since the request is to modify board in-place
            we come up with a notation that indicates orig & target values
            design our calculations around the made up notation
        in this case the notation is as follows
            orig    new    translation
            0       0       0
            1       0       1
            0       1       2
            1       1       3
        
        after reading the prob desc we come to conclusion that
            if orig value is 1 & count is 2 or 3
                update value to 3
            if orig value is 0 & count == 3
                update value to 2
        
        we need to take the above values into consideration while calcuating the count of adjacent nodes
"""
```

