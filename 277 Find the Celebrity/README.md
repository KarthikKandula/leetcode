# 277. Find the Celebrity

1 possible solution for this problem  


```
"""
    this is a classic graph traversal and elimination problem
        this focuses on reducing search space efficiency
        the nodes are directed i.e directed edges
        first we eliminate non celebrities in one pass
            we check all nodes one by one with a possible celebrity candidate
            if any candidate knows any node
                it's not a celebrity
                the new node becomes a celebrity candidate now
            doing this until end, leaves us with one celebrity candidate
        now we confirm if this candidate is indeed a celebrity
            to be a celeb, this candidate shouldn't know anyone
            and everyone else should know this candidate
            if at anytime this condition is breached
            return there is no celeb
"""
```

