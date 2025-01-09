# 75. Sort Colors

1 possible solution for this problem  


```
"""
    to do the same operation with using extra space
        since there are only two colors, we use that to our advantage
        we track the first & last color using pointers at either end
        if we encounter the first color
            place in in first pointer location & increment the pointer
        if we encounter the last color
            place in in last pointer location & decrement the pointer
            while doing this, we also handle an edge case
                incase the value being replaced is a 0 or 1, we need to process it again
                so we decrement i pointer to keep it in the same place
        by the end, colors will be sorted        
"""

"""
    use a hashmap to count number of occurrences of each value
        loop thru input array
            check the count of a particular color 
                if it is not 0, place that color in the location 
                repeat for each color, until their counts are exhausted
"""
```

