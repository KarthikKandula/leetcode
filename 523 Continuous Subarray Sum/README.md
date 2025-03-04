# 523. Continuous Subarray Sum

1 possible solution for this problem  


```
"""
    Optimal prefix sum solution

    due to the properties of modulus operator
        it is okay to keep one running remainder 
        as opposed to trying out all sum possibilities 
        then checking if the remainder is 0 at every element
    
    so in plain simple words, we keep adding numbers to remainder & perform modulus operation
        keep track of the modulus values along with indexes
        if a modules value appears again
            it means there was a subarray of sum k that is in between
            so we check for the difference in indexes between current index & prev index
"""
```

