# 338. Counting Bits

2 possible solution for this problem  

### Self Notes


```
"""
    the idea behind this is to use values previously calculated to count future values
        the way bit operations work is patterns repeat for every base 2 levels (1,2,4,8 etc.,)
        so by reusing the value previously calculated & adding 1 to it, we get the new 1's count

        by doing this we're solving the problem in single pass
"""

"""
    Loop thru each number from 0 to n & perform & for n & n - 1

    the idea behind this is to bit & the number n to n - 1
        by doing this, we'll be slowly removing all 1's in the number
        and since it's an and(&) operation, any 1's that have any mismatches will be made to 0's
        the pro in this method is that the loop won't run 32 times (since 32 bit integer)
            once all the values are 0, loop will stop
"""
```

