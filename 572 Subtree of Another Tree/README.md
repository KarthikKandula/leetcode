# 572. Subtree of Another Tree

1 possible solution for this problem  

## Method 1 (Recursive approach)

To determine if one tree (`subRoot`) is a subtree of another (`root`) using a recursive DFS approach, follow these steps:

### Steps

1. **Create a Helper Function**:
   - Implement a helper function that checks if two trees are the same.
   - This function should compare the values of the current nodes and recursively check their left and right children.

2. **Handle Edge Cases in the Main Function**:
   - If `subRoot` is `None`, return `True` (an empty tree is a subtree of any tree).
   - If `root` is `None`, return `False` (a non-empty tree cannot be a subtree of an empty tree).

3. **Check if Trees are the Same**:
   - Use the helper function to check if the current `root` tree and `subRoot` tree are the same.
   - If they are, return `True`.

4. **Recursive Calls**:
   - If the trees are not the same, recursively call the main function on the left and right subtrees of the current `root`.
   - Pass `root.left` and `subRoot`, and then `root.right` and `subRoot` to check all possible positions where `subRoot` might be a subtree of `root`.

5. **Return the Result**:
   - The result of these recursive calls determines if `subRoot` is a subtree of `root`.

### Conclusion

This approach efficiently checks for the presence of a subtree using recursion and DFS, with a time complexity of O(m * n), where `m` and `n` are the number of nodes in `root` and `subRoot`, respectively.

### Self Notes
To solve this problem, we can use basic implementation of recursive dfs. if we break the problem into subproblems, it is the same tree problem all over again. to make it easier, create a helper function that implements same tree algo. now for the main function, we handle couple edge cases first, like if subRoot is none -- can be subtree of any node, return True, if root is none -- no tree can be subree, return false. now check if current Tree are subTree are the same by calling the helper function. if not, make a recursive call to main function but now pass tree's left subtree & right subtree, so we're doing the comparision all over again

```
"""
   to solve this problem use basic tree dfs tree traversal with a couple additional steps
      breaking up this problem into subproblems reveals this is the Same Tree problem
      we need to check if root & subRoot are the same tree at any given node
         if they are not, check for root's left & right nodes with entire subRoot

      for this, create a helper function that implements same tree algorithm

   in the main function
      cover couple edge cases like
         if subRoot is none -- can be subtree of any node, return True
         if root is none -- no tree can be subree, return false

      check if trees are same at current node
         if not recursive call same function with left & right nodes but entire subRoot 
"""
```
