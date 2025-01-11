# 310. Minimum Height Trees

1 possible solution for this problem  


```
"""
    optimal solution

    the way minimum height trees work is that there can only be 1 or 2 MHT's
        cuz if there is a tree with 3 nodes of equal height values, the middle node is the MHT
        using this logic, we can come to the conclusion that if we start removing leaf nodes
            iteratively remove leaf nodes
            in the end, there will only be 1 or 2 nodes left & those nodes will be the MHT
            keep eliminating leaf nodes
                in the process if any new leaf nodes are created, eliminate them as well
                only 1 or 2 nodes will be remaining, those are the MHT's

        build an adjacency list
        build an array with no of connections in a diff array -- heights
        get all nodes with only 1 connection in the queue
        process each node & reduce the count of neighbors from heights array
            if any neighbor's height becomes 1, add it to the queue
            if the remaining node's become 1 or 2, those are the MHT's, return a list with these nodes
"""
```

