# 402. Remove K Digits

1 possible solution for this problem  


```
"""
    this is a classic mono decreasing problem with a couple twists
        since we need to remove k digits to make the value as low as possible
        we remove values that are out of place
            i.e., where their next values are greater
            since this value is high than it's next, we remove it the value comes down the most compared to others
        to implement this, we can use mono decreasing stack to implement
            remove values from stack and decrement k values 
                to only remove k digits
            handle the leading 0's edge case by not inserting into stack when it's empty
        in the end, combine all values from stack and return
"""
```

