# 235. Lowest Common Ancestor of a Binary Search Tree

2 possible solutions for this problem  
 - Iterative & Recursive approach

## Method 1 (Iterative approach)

To find the Lowest Common Ancestor (LCA) of two nodes (`p` and `q`) in a BST, use the following approach:

### Steps

1. **Utilize BST Characteristics**:
   - In a BST, the left child is always less than the parent, and the right child is always greater than the parent.
   - This property allows us to decide whether to search in the left or right subtree based on the values of `p` and `q`.
2. **Tree Traversal**:
   - Start traversing the tree from the root node.
   - At each node, compare its value with `p` and `q`:
     - If the current node’s value is less than both `p` and `q`, move to the right subtree.
     - If the current node’s value is greater than both `p` and `q`, move to the left subtree.
3. **Determine the LCA**:
   - If one of `p` and `q` is in the left subtree and the other is in the right subtree, the current node is the LCA.
   - This is because, at this point, moving further in any subtree would not contain both nodes.
4. **Return the LCA**:
   - When you find the node where one value is in the left subtree and the other in the right (or if the node itself matches one of the values), return that node as the LCA.

### Conclusion
This method efficiently finds the LCA in a BST using its properties, ensuring a time complexity of O(h), where `h` is the height of the tree.

### Self Notes
To solve this problem, we can use basic tree traversal with couple twists. the input is a bst, which means left is less than parent & right is greater than parent. if we break the problem into subproblems, we need to make a decision whether to search in left or right subtree. we can use bst characteristics to our advantage, if curr node is less than p & q it means we need to search in right subtree, if they are greater search in left subtree. if one value is in left & one value is in right, it means that is the LCA since going into any subtree at that point, we wouldn't find either p or q. return that value as LCA

```
"""
   Iterative solution

   we can solve this problem using basic tree traversal
      the twist here is, input is a bst
         means left node is less than parent & right node is greater than parent
      we can use bst characteristics to effectively search for LCA

   the idea is to reduce the problem to making a decision on which subtree to search in 
      Check if curr node value < than p & q
         check the right subtree
      Check if curr node value > than p & q
         check the left subtree
      Else
         LCA is the curr node
         This else covers below 
               If curr value is > than one & < than the other
               Or equal to one & > than one or < than the other
         It means this is the LCA, we don't have to look further
"""
```

## Method 2 (Recursive approach)

need to learn