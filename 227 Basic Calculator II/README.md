# 227. Basic Calculator II

1 possible solution for this problem  


```
"""
    we use a stack to solve this problem
        the basic idea is to solve multiplication and division first, so it's solved immediately
        when encountering a + or - operator
            insert the num with the sign into the stack 
        so that the numbers are in stack with their sign
            once multiplication & division are solved
            sum the values in stack & we get the answer
"""
```

