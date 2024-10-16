# 98. Validate Binary Search Tree

1 possible solutions for this problem  

## Method 1

To determine if a binary tree is a BST using a recursive approach, follow these steps:

### Steps

1. **Define the BST Property**:
   - In a BST, all nodes in the left subtree must be less than the node’s value, and all nodes in the right subtree must be greater.

2. **Use Recursive Tree Traversal**:
   - A recursive approach is suitable as it allows easy comparison of each node's value while maintaining the constraints defined by its ancestors.
   - Create a helper function that accepts the current node and two boundaries: `low` and `high`.
     - `low`: the minimum allowable value for the current node.
     - `high`: the maximum allowable value for the current node.

3. **Check Node Validity**:
   - At each node, check if its value is within the allowed range (`low < node.val < high`).
   - If the node's value is outside these bounds, return `False`.

4. **Recursive Calls for Subtrees**:
   - Recursively call the function for the left child with updated boundaries (`low` remains the same, `high` becomes the current node's value).
   - Recursively call the function for the right child (`low` becomes the current node's value, `high` remains the same).

5. **Return the Result**:
   - The function returns `True` only if both the left and right subtrees return `True`.
   - The root node’s function call will determine if the entire tree is a valid BST.

### Conclusion
This approach validates whether the tree is a BST in O(n) time, where `n` is the number of nodes, ensuring that each node is checked once.


### Self Notes
To solve this problem, we can use basic recursive tree traversal. the decision to make it recursive is since we need to compare values from down the nodes in the tree, recursive functions make it easy. the problem is to identify whether the input is a bst, to achieve this we need the allowable limit in which that node's value can be i.e., low & high values. at that point it is easy to compare these values & decide if that node is a bst or not. since this is recursive, it automatically happens for each node, at the end of each recursive function we return True if left subtree & right subtree are both True, else False. root node's return value will have result for the entire tree 


```
"""
   we can solve this using basic tree traversal with a slight twist
      the problem is to check if input is a valid bst
      for this, we need to keep track of the min & max values that any particular node is allowed to be in

   create a recursive function that takes node, low & high values
      check if curr node's value is between low & high
         if not, return False
      recursive call to left subtree
         since left node is supposed to be less than parent node
         change high value in func call to parent node's value
      recursive call to right subtree
         since right node is supposed to be greater than parent node
         change low value in func call to parent node's value

      function return value is True/False -- if that node is valid & is a bst or not
         we need all function return values to be Tre
      return True if left subtree & right subtree are bst's
         else False

   root node's return value is the answer to whether the tree is bst
"""
```

