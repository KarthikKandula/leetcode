# 394. Decode String

1 possible solution for this problem  


```
"""
    this is a classic stack problem
        we need to process things in stack in a certain manner
        get the characters to be repeated 
        get the number of times those chars have to be repeated
        insert all values into the stack
        once a closing brace has been encountered
            we need to process the last string
            find all chars until a [ is hit -- last point for current chars
            find all nums until a char is hit -- last point for current nums
            repeat char num times & add to stack
        do this until the end, we have our result in the stack
"""
```

