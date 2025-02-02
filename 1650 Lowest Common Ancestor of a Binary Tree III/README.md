# 1650. Lowest Common Ancestor of a Binary Tree III

1 possible solution for this problem  


```
"""
    the idea is to implement the intersection of two linked lists algorithm to this
        we need the node that's common in p & q's path to root
        instead of saving the path in a set
            we can use the depth aka the no. of nodes between p/q to root
        by using depth values we know the no. of nodes each node is seperated from the root
        now, we move the nodes to make them equal in depth from the root
        after their depth's match, move each towards the root in one step at a time until they meet
        once they meet, that node is the LCA
"""
```

