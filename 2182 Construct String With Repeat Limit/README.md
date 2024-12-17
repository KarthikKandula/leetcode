# 2182. Construct String With Repeat Limit

1 possible solution for this problem  

### Self Notes


```
"""
    Polished solution
        My solution in polished code

    can solve this problem using maxHeap & counter
        get the max value from heap in every loop 
            add the character to output max allowed times & see if it has to be inserted back into the heap
            if this value still has remaining count
                get the next value from heap
                add it once to the output, so as to not violate the repeatLimit
        by doing this we're reducing the no. of iterations
"""
```

