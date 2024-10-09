# 110. Balanced Binary Tree

1 possible solution for this problem  

## Method 1

To determine if a binary tree is height-balanced using a recursive DFS approach, follow these steps:

### Steps

1. **Define the Return Value**:
   - Modify the return value of the helper function to be a list containing:
     - A boolean indicating whether the node is balanced (`True` or `False`).
     - The maximum height of the node.

2. **Create the Helper Function**:
   - Implement a recursive helper function that:
     - Checks the balance of the current node.
     - Computes the maximum height of the node.

3. **Recursive Logic**:
   - In the helper function:
     - If the current node is `null`, return `[True, 0]` (indicating that it is balanced and has a height of 0).
     - Recursively call the helper function for the left and right children to get their balance status and heights.
     - Determine if the current node is balanced by checking:
       - The absolute difference between the heights of the left and right subtrees is less than or equal to 1.
       - If the left or right subtree is unbalanced (i.e., either returned `False`).
     - Return `[True/False, max_height]` based on the balance status of the current node and its height.

4. **Invoke the Helper Function**:
   - Start the process by calling the helper function on the root of the tree.

5. **Return the Result**:
   - The balance status of the entire tree can be determined by checking the value returned for the root node.

### Conclusion

This approach efficiently checks if the binary tree is balanced in a single traversal, achieving a time complexity of O(n).

### Self Notes
To solve this problem use dfs recursive approach, we need two things at each node, if that node is balances & the max height of the node so parent nodes can calculate if they're balanced or not. to facilitate this, we'll modify the return value to become [balanced or not -- True/False, max height of the node]. in each iteration after getting responses for left & right subtree, check if node is balanced, subtract left & right height -- if not less than or equal to 1, send False if return value along with max height of that node. this way parent nodes also know there is a unbalanced node below which automatically makes them unbalanced. in the end return the value for root


```
"""
   we can solve this using dfs recursive approach with a slight twist
      modify the return value -- returning [boolean (if tree is balanced), max height of subtree]

   in recursive function
      make function calls for left & right subtrees
      check if tree is balanced for that node
         check the first element of response -- boolean
         check the difference between left & right values -- should be less than or equal to 1
         if they're not, in the return value put false -- if this is false none of the other parent nodes will be true
      return with [True/False, max height of subtree]

   in the end return the helper function response -- the first element that is boolean
"""
```
