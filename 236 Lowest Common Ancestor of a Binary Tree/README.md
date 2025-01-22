# 236. Lowest Common Ancestor of a Binary Tree

1 possible solution for this problem  


```
"""
    we can solve this using dfs tree traversal
        since we need to find two nodes & the LCA for both nodes
        we need the latest node where both nodes have been found
            so if both nodes are found at any node, that node is the LCA, return that node
        if both nodes are in a single sub-tree
            we need to return the highest placed node as the LCA
        if a node doesn't match either p or q
            search left & right tree
            if left tree isn't found
                return right node as the LCA 
                since it means both nodes exist in the right tree
            same with right
"""
```

