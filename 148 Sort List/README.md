# 148. Sort List

1 possible solution for this problem  


```
"""
    using MergeSort

    the basic idea of the problem is to apply merge sort to the linked list
        merge sort involves breaking the input into two equal parts
            until we have individual nodes
            at this point we can start combining nodes in a sorted manner
                use two pointer comparision technique
            keep doing this until the entire list is formed
        
        the only twist here being to find the mid point in every linked list
            we need to start fast pointer at fast.next -- just to reach the right mid point
"""
```

