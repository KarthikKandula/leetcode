# 162. Find Peak Element

1 possible solution for this problem  


```
"""
    we can solve the problem using binary search (modified binary search)
        solving the problem in linear time is simple & easy
        but solving in O(log n) is challenging
        
        the important pieces of info that is useful for bin search is
            no two values are the same
            the ends are -inf, which means inside value is the higher value
        if we consider both these statements, we can deduce that
            a peak element is only followed by lesser numbers
            so when we find a mid point
                if the left value is higher, there is possiblity that a peak element exists on that side
                    even if no values exist on that side
                    we can conclude that if it's the end of array or there are only less values after that
                    that value will still be the peak element
                same with right value is higer
            so by going towards whatever is the higher value at every mid point
            we can find a peak element
"""
```

