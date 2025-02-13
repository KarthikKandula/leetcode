# 901. Online Stock Span

1 possible solution for this problem  


```
"""
    this is a classic monotonic stack problem
        if we look at the problem seriously
            it's a previous greater element problem in disguise
        the twist in this problem is that, we'll have a continuous stream of data coming in
            having to constantly update our stack & derive answers from it
        but to our advantage, we only have to return values that are less than or equal to current values
            this is what monotonic stack implements bloody well
        we remove values from stack that are less than or equal to current value
            once all values are removed, get the top value in stack
                this is the highest value above current price
                get the difference between current index & the higher value index
                it's the answer
"""
```

