# 105. Construct Binary Tree from Preorder and Inorder Traversal

1 possible solution for this problem  

## Method 1

To construct a binary tree using pre-order and in-order traversal arrays, follow these steps:

### Steps

1. **Utilize Characteristics of Pre-Order and In-Order Traversals**:
   - In a pre-order traversal, the root node is always the first element.
   - In an in-order traversal, all nodes to the left of the root are part of the left subtree, and all nodes to the right are part of the right subtree.

2. **Recursive Approach**:
   - Recursion is the simplest way to build the tree since each node requires building its left and right subtrees independently.
   - Create a helper function that will take the current bounds of the pre-order and in-order arrays to construct subtrees.

3. **Identify the Root Node**:
   - The first element of the pre-order array is the root node.
   - Locate this root node in the in-order array to determine the boundaries of the left and right subtrees.

4. **Build Left and Right Subtrees Recursively**:
   - Using the index of the root node in the in-order array:
     - Recursively call the helper function for the left subtree (elements before the root in the in-order array).
     - Recursively call the helper function for the right subtree (elements after the root in the in-order array).

5. **Return the Root Node**:
   - Create the root node and connect the left and right subtrees returned from the recursive calls.
   - Return the root node, which becomes the connection point for each subtree and ultimately constructs the entire tree.

6. **Repeat Until Tree is Fully Built**:
   - The base case for the recursion is when there are no elements left in the current subtree segment.

### Conclusion
This recursive approach constructs the binary tree efficiently using the properties of pre-order and in-order traversals, ensuring a time complexity of O(n), where `n` is the number of nodes.


### Self Notes
To solve this problem, we use both in-order & pre-order inputs together & their charecteristics to our advantage. in pre-order traversal, root node always comes first & in-order traversal is in a way that everything to left of the root node is part of left subtree & everything to right is part of right subtree. We use this knowledge to our advantage. this solution is going to be a recursive one since we need to be building left & right subtree for each nodes individually, hence recursion is the simplest way to go. get root node from pre-order, create a node for that & make recursive calls for left subtree & right subtree. return root at the end. since returning root for each, these return values from each recursive function automatically creates the connection to left & right of each node.


```
"""
   Everything to the left of root in inorder is the left subtree
   Everything to the right of root in inorder is the right subtree
"""
```

