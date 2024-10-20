# 124. Binary Tree Maximum Path Sum

1 possible solution for this problem  

## Method 1

To find the maximum path sum in a binary tree using a recursive DFS approach, follow these steps:

### Steps

1. **Use Recursive DFS**:
   - The problem requires calculating values at each node and passing information up the tree to parent nodes, making recursion the simplest and most effective approach.

2. **Define Two Key Values for Each Node**:
   - **Max Path Value at the Current Node**:
     - Calculate the maximum path sum that can be achieved at the current node by considering the node's value and the maximum contributions from its left and right children.
     - Update a global `result` variable with this value if it's the highest encountered so far.
   - **Max Sum to Return**:
     - Return the maximum sum of either the left or right subtree plus the current node’s value.
     - This value will be used by the parent node to calculate its own maximum path value.

3. **Recursive Calculation**:
   - For each node:
     - Recursively call the function on the left and right children to obtain their maximum contributions.
     - Calculate the max path value for the current node and update the `result` variable.
     - Return the max sum (left or right) plus the current node’s value to the parent.

4. **Return the Final Result**:
   - After all nodes have been visited, the global `result` variable contains the maximum path sum of the entire tree.
   - Return this `result` at the end.

### Conclusion

This recursive approach efficiently computes the maximum path sum in a binary tree with a time complexity of O(n), where `n` is the number of nodes in the tree.


### Self Notes
To solve this problem, we use recursive dfs with added logic & code. the solution is going to be recursive since we need to calculate values at each node & return values to parent nodes where the calculations happen again. hence recursion is the simplest way to go. we need two things for each node here, 1. calculate the max path value at current node & update result variable 2. return the max sum so parent node can use it (max of left & right at current node). once the algo visits all nodes, result is stored in result variable, which is returned at the end


```
"""
   use dfs recursive traversal with extra logic to solve the problem
      we need to update the max sum at any node
      get the max sum for left & right subtrees
   
   use a recursive function to effectively implement
      get the max value for left subtree
         if value is negative, replace with 0
      get the max value for right subtree
         if value is negative, replace with 0
      
      calculate max path value for current node -- curr.val + left + right
         replace global result variable with max value

      return curr.val + max of left, right subtree
         since we only need one path's value
   
   return result variable at the end
"""
```

