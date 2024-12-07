# 190. Reverse Bits

1 possible solution for this problem  

### Self Notes


```
"""
    the idea is to extract all the values in input one digit at a time,
    and insert them back in reverse order 1 digit at a time

    extracting values one digit at a time
        right shift n with each number until range i & then and with 1
        gives the right most value

    insert them back in reverse order
        create a result array with initial value 0
        take the right most value from above & or it with result array -- OR preserves all 1's already in result
        since we need to insert them in right order, left shit it by 31 - i (i is the location where to insert)

    essentially we're getting a location from right & insert it in the same location from left 
        so on opposite sides of the spectrum
"""
```

