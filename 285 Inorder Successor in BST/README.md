# 285. Inorder Successor in BST

1 possible solution for this problem  


```
"""
    we use an implementation of in-order traversal in this problem
        we can use bst characteristics to implement this easily
        to find any successor, we have to eliminate either left or right subtree
        if current value is less than target p value
            we search in right tree, eliminate left tree
        if current value is greater than target p value
            search in left tree, eliminate right tree
"""
```

