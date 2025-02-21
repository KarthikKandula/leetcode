# 69. Sqrt(x)

1 possible solution for this problem  


```
"""
    we can solve this problem using binary search
        basically check for each number from 0...x to see which value is the square root
        to make this more efficient, we can use binary search
            with each calculation, eliminate half of the values
            the highest value where the square root is less than target is the result
                unless an exact root has been found
"""
```

