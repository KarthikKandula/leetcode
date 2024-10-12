# 100. Same Tree

2 possible solution for this problem  
- Iterative & Recursive approach

## Method 1 (Iterative approach)

To determine if two binary trees are equal using an iterative BFS approach, follow these steps:

### Steps

1. **Initialize a Queue**:
   - Use a queue to store pairs of nodes from both trees for comparison.
   - Start by enqueuing the root nodes of both trees as a pair.

2. **Iterate Through the Queue**:
   - While the queue is not empty, dequeue a pair of nodes.

3. **Compare Nodes**:
   - If both nodes are `null`, continue to the next iteration (they are equal).
   - If one node is `null` while the other is not, return `False` (they are not equal).
   - If the values of the nodes are not equal, return `False`.

4. **Enqueue Left and Right Children**:
   - Enqueue the left children of the current node pair.
   - Enqueue the right children of the current node pair.
   - This ensures nodes from similar positions are together in the queue for easy comparison.

5. **Complete the Iteration**:
   - If the queue is processed without finding any inequality, return `True`.

### Conclusion

This approach uses an iterative BFS technique to compare the two trees efficiently, ensuring that all corresponding nodes are compared in pairs with a time complexity of O(n).

### Self Notes
To solve this problem using Iterative approach, we can use basic implementation of bfs with added code to compare values for each node.  
the twist is push to queue in pairs, so nodes from similar positions are together in queue -- easier for comparision, compare if both nodes are equal -- null is equal, if one node has a value & the other doesn't -- not equal - return false, insert left node pair & right node pair to queue

```
"""
   Iterative solution

   we use basic bfs iterative traversal to solve this problem
      the twist is push to queue in pairs, so nodes from similar positions are together in queue -- easier for comparision
         compare if both nodes are equal -- null is equal
         if one node has a value & the other doesn't -- not equal - return false
         insert left node pair & right node pair to queue
"""
```

## Method 2 (Recursive approach)

To determine if two binary trees are equal using a recursive DFS approach, follow these steps:

### Steps

1. **Define the Base Cases**:
   - If both nodes are `null`, return `True` (they are equal).
   - If only one node is `null` while the other is not, return `False` (they are not equal).

2. **Compare Node Values**:
   - Check if the values of the current nodes in both trees are the same.
   - If they are not equal, return `False`.

3. **Recursive Calls**:
   - Recursively call the function for the left subtree of both trees.
   - Recursively call the function for the right subtree of both trees.

4. **Return the Result**:
   - Return `True` only if all the conditions for equality are met (both left and right subtrees must also return `True`).
   - Return `False` if any of these checks fail.

5. **Invoke the Function**:
   - Call the recursive function starting with the root nodes of both trees.

### Conclusion

This approach allows for an efficient comparison of two binary trees, ensuring that all nodes are checked for equality with a time complexity of O(n).

### Self Notes
To solve this problem using Recursive approach, we can use basic implementation of dfs of recursion with added code to compare values for each node. in each function call, we need to do below things, compare if both nodes are equal -- null is equal, if one node has a value & the other doesn't -- not equal - return false, perform recursive function call for left & right trees, return true if all true conditions are met, return false if even one false condition is met

```
"""
   Recursive solution

   we use basic dfs recursion algorithm with a change to return values
      in each function call, we need to do below things
         compare if both nodes are equal -- null is equal
         if one node has a value & the other doesn't -- not equal - return false
         perform recursive function call for left & right trees
         return true if all true conditions are met
         return false if even one false condition is met
"""
```
