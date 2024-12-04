# 66. Plus One

1 possible solution for this problem  

### Self Notes


```
"""
    Optimal solution

    idea behind this solution is to use addition to our advantage
        if all we're doing is adding 1, it's added to the last digit 1st
        if there needs to be a carry then it's added to next digit
        we use this knowledge 
    
    loop thru the input in reverse order
        if a digit is less than 9, we can add 1 to that place & return result
            this by default works for any no. of 9's in the input
        if a digit is 9, that location should be made 0 & 1 to be added to next location
    
    one edge case to be taken note of is if the inputs are all 9's, in the end we return with 1 added to the front
"""
```

