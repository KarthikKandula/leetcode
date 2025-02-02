# 1644. Lowest Common Ancestor of a Binary Tree II

1 possible solution for this problem  


```
"""
    The idea is to see if both nodes are in the tree while finding their LCA
        implementing a plain LCA exits if it find either of the nodes
            if it's not able to find it in a parallel subtree
            it means the first found node is the LCA & the other node is it's child
        we need to make sure to search again for the other node in the first found node
        just call the recursive function again
            search in first found node's left & right trees
        doing this we're not doing any double work since we're traversing all nodes only once
"""
```

