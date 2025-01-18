# 61. Rotate List

1 possible solution for this problem  


```
"""
    we can solve this using basic linked list traversal
        to rotate the list by k places
            we need the last node
            and length of the list
        use a pointer to traverse thru the list
            to point at last node
            also to get the length of list
        
        if we have to rotate the list by k places
            we need to get the node at length - k - 1 location
            the next node at this position is going to be the new head node
        loop thru the input again, to get to new head node
            kill connection with next node
            establish connection with last node to head node
    
    return new head node in the end
"""
```

