# 189. Rotate Array

1 possible solution for this problem  

### Self Notes


```
"""
    O(1) space solution

    the idea for a constant space solution is to
        if we observe any example after the array is rotated we observe a pattern
        reverse the entire array
        reverse k elements (first k values)
        reverse n - k elements (last remaining values after k)
    
        also another thing to note is that k can be potentially reduced if we mod it with length of input

    if we do this we'll end up with the rotated array
"""

"""
    O(N) space solution

    moving a value to the next k digits & storing the value at target in a hashmap
    doing this solves the problem but also uses O(N) space since hashmap can have all the values
"""
```

