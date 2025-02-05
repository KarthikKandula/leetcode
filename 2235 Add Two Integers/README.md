# 2235. Add Two Integers

1 possible solution for this problem  


```
"""
    to solve this problem without using any operators
        we need to use bitwise operators to solve this
        first, determine if there is a carry to be moved 
            carry can be extracted by using &
        second, perform additions without any carry
            this can be done using bitwise XOR ^
        next, move carry to the next location
            by shifting it 1 place to the left
            using << operator
        once carry becomes 0, we have our sum in the variable using to perform additions 
"""
```

