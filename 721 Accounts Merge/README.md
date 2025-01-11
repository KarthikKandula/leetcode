# 721. Accounts Merge

1 possible solution for this problem  


```
"""
    this problem can be solved using a dfs graph traversal
        we need to find connected components between emails
        if we think of emails as nodes, then the connections between them determines if they belong to the same user
        so while building an adjacency list, we use the first email as a base node
            something to base the connections out of
            we can't use the user since there can be multiple different users with same name
            we'll use the first email here but we can use any email in the list
                serves the same purpose
        after building the adjacency list, we need extract common connections based on our list
            let's implement a dfs graph traversal algo with post-order traversal
            call the recursive function for each email in input & build an array of connected components for each
            keep a visited set handy to avoid loops & duplicate outputs
        recursive function
            add the current node to visited
            loop for each neighbor in the adjacency list & call for neighbor
            once all neighbors are visited, add to result (post order traversal)
"""
```

