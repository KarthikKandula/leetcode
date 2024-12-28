# 106. Construct Binary Tree from Inorder and Postorder Traversal

1 possible solution for this problem  

### Self Notes


```
"""
    we can solve this problem combining factors of inorder & postorder together
        root node is always the last in postorder
        everything to the right of root is right subtree
            vice versa to left subtree
        if we breakdown the problems into subproblems passing shorter inputs
            a tree is going to be built eventually
"""
```

