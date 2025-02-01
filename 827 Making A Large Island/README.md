# 827. Making A Large Island

1 possible solution for this problem  


```
"""
    this is an extension of the largest island problem
        to solve the problem
        we need to first know all the islands
        then find out by flipping which 0 value, we can form the biggest island

        get all islands & their r, c values in a hashmap
            assign a unique identifier to each island
        record the size of each island via it's unique identifier

        go thru each 0 & check it's 4-directional values
            sum sizes of everything & check if it's the max
        
        in the end, return the max value
"""
```

