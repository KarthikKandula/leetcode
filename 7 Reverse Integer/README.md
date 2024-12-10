# 7. Reverse Integer

1 possible solution for this problem  

### Self Notes


```
"""
    the idea is to
        get each digit from one's place by using remainder operation
        update x by dividing with 10, to remove above digit

        check if until that point result value has a chance of overflowing
            check if it's greater than the MAX value & is it going to be greater than max value after adding current digit
            same with MIN
        
        if not going to overflow, add to result & repeat loop
    
    in the end return result value
"""
```

