# 160. Intersection of Two Linked Lists

1 possible solution for this problem  


```
"""
    the basic idea is to apply linked list traversal in creative ways
        to get the intersecting node without using any extra space
        we need to get the distance of each list to the end
        start from the same location from the end
            move each lists one node at a time
            if they meet, they'll meet at the same node at some point
            this node is the intersecting point
            
            if they don't meet, any of the list is going to become null
            hence we know the two lists never meet
"""
```

