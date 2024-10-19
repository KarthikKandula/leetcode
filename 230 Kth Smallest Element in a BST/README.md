# 230. Kth Smallest Element in a BST

1 possible solutions for this problem  

## Method 1

To find the k-th smallest element in a binary search tree (BST) using in-order traversal, follow these steps:

### Steps

1. **Utilize BST Characteristics**:
   - In a BST, an in-order traversal (left -> root -> right) produces nodes in ascending order.

2. **Use an Iterative In-Order Traversal**:
   - Implement the traversal using a stack to keep track of nodes (standard DFS approach).
   - This method allows you to efficiently traverse the tree while maintaining the order of elements.

3. **Track Nodes Visited**:
   - Use an integer variable (`count`) to keep track of the number of nodes visited during the traversal.
   - Initialize `count` to 0.

4. **Perform the In-Order Traversal**:
   - While traversing:
     - Move to the leftmost node, pushing nodes onto the stack.
     - Pop the stack, increment the `count`, and check if `count` equals `k`.
     - If `count` equals `k`, return the value of the current node (as it is the k-th smallest element).
     - If not, move to the right subtree and continue.

5. **Return the k-th Smallest Value**:
   - The value returned when `count` equals `k` will be the k-th smallest element in the BST.

### Conclusion
This approach leverages the sorted order of BSTs and efficiently finds the k-th smallest element with a time complexity of O(h + k), where `h` is the tree height.


### Self Notes
To solve this problem, we can use in-order tree traversal. input is a binary search tree, we use bst's characteristics to our advantage. problem is to find kth element in a bst, since bst's values are always in sorted order -- if done an in-order traversal, use a stack to keep track of nodes -- standard dfs solution, use a int variable to keep track of num of nodes visited, at any point if count == k (input) -- return that value


```
"""
   we can solve this problem using in order tree traversal
      input is a binary search tree, we use bst's characteristics to our advantage

      problem is to find kth element in a bst
         since bst's values are always in sorted order -- if done an in-order traversal

   use a stack to keep track of nodes -- standard dfs solution
   use a int variable to keep track of num of nodes visited
      at any point if count == k (input) -- return that value

   loop while stack has values or curr node is valid
      check if curr node is valid
         if it is, we need to go further left
      if curr node is not valid
         pop last node from stack & visit it
         increment count value
         check if count == k (input)
               return than value if yes
         if not, shift curr right since we need to go further right
"""
```

