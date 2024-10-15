# 1448. Count Good Nodes in Binary Tree

1 possible solutions for this problem  

## Method 1

To count the number of good nodes in a binary tree using a recursive approach, follow these steps:

### Steps

1. **Define Good Nodes**:
   - A node is considered "good" if no node along the path from the root to that node has a value greater than the node’s value.

2. **Use Recursive Tree Traversal**:
   - The recursive approach is suitable as it allows easy comparison of node values from the root down to the leaves.
   - Create a helper function that tracks the maximum value encountered along the path from the root to the current node.

3. **Compare Node Values**:
   - At each node, compare its value with the maximum value seen so far on its path.
   - If the node’s value is greater than or equal to this maximum value, it is a "good" node.
   - Update the maximum value when moving to the node’s children.

4. **Count Good Nodes**:
   - For each node, recursively call the function for the left and right children, passing the updated maximum value.
   - Return the sum of good nodes found in the left subtree, right subtree, and the current node itself (`1` if it’s a good node, otherwise `0`).

5. **Return the Result**:
   - The root node’s recursive call will return the total number of good nodes in the entire tree.

### Conclusion
This approach efficiently counts good nodes in a binary tree with a time complexity of O(n), where `n` is the number of nodes in the tree, ensuring each node is visited once.


### Self Notes
To solve this problem, we can use basic recursive tree traversal. the decision to make it recursive is since we need to compare values from down the nodes in the tree, recursive functions make it easy. the problem is to identify good nodes in tree, good nodes are defined if there is no node in it's path to root that is greater than itself, to achieve this we need the max value in it's path to root for each node, at that point it is easy to compare these values & decide if that node is good or not. since this is recursive, it automatically happens for each node, at the end of each recursive function we return left + right + 1 (if that node is good), 0 (if that node is not good). root node's return value will have the no. of good nodes for the entire tree 


```
"""
   we can solve this problem using basic tree traversal with a slight twist
      the problem is to check if any particular node if greater than every other in it's path to the root node
      for this, we need to have the max value in path available to us

   create a recursive function that takes the max value & curr node
      check if curr node's value is greater than or equal to maxValue 
         if it is, increment temp variable
      recursive call left subtree
      recursive call right subtree

      return left + right + curr node's temp variable
   
   root node's return value would have good node count for the entire tree
"""
```

