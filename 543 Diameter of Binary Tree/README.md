# 543. Diameter of Binary Tree

1 possible solution for this problem  

## Method 1

To find the diameter of a binary tree using a recursive DFS approach, follow these steps:

### Steps

1. **Initialize a Global Variable**:
   - Create a global variable to store the maximum diameter of the tree.

2. **Define a Helper Function**:
   - Implement a recursive helper function that:
     - Calculates the maximum depth of the left and right subtrees.
     - Updates the global maximum diameter using:
       - `max_diameter = max(max_diameter, left_depth + right_depth)`
     - Returns the maximum depth at the current node.

3. **Implement Recursive Logic**:
   - In the helper function:
     - If the current node is `null`, return `0` (base case).
     - Recursively call the helper function for the left and right children.
     - Update the global maximum diameter with the sum of the depths from both children.
     - Return the maximum depth of the current node to its parent.

4. **Invoke the Helper Function**:
   - Start the recursive process by calling the helper function on the root of the tree.

5. **Return the Result**:
   - The maximum diameter will be stored in the global variable, which can be returned as the final result.

### Conclusion

This method allows for the efficient calculation of the binary tree's diameter in a single traversal, achieving a time complexity of O(n).

### Self Notes
To solve this problem use dfs recursive approach, we need two things at each node, the max diameter which is max depth of left + max depth of right and also we should be returning the max depth at each node so the parent can calculate max diameter. so for this we'll make max diameter a global variable & create a helper function that implements recursive dfs. calculates max diameter at each node, updates the global variables & returns max depth at each node. in the end, max diameter is in the global variable which we return

```
"""
   solve the problem using dfs recursive approach
      since we need left & right values to be returned first
   
   take a helper function to help with the recursive dfs functions
   also need a variable to store the maxDiameter -- make this a global variable

   in helper function
      get max depth of each subtree, left & right
      max diameter at that node is left + right, update global variable with max value
      return max depth at this node to help calculate maxDiameter for parent node

   return max diameter (global variable) in the end
"""
```
