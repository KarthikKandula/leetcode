# 4. Median of Two Sorted Arrays

2 possible solution for this problem  
- Iterative & Recursive approach

## Method 1 (Iterative approach)

To invert a binary tree using an **iterative approach**, we use a **Breadth-First Search (BFS)** traversal with a queue. The goal is to swap the left and right children of each node as we traverse the tree.

#### Steps:

1. **Initialization**:
   - Use a queue to keep track of nodes to be processed. 
   - Start by adding the root node to the queue.

2. **Breadth-First Search (BFS) Traversal**:
   - While the queue is not empty:
     - Remove the front node from the queue.
     - Swap its left and right children.
     - If the swapped left child is not `null`, add it to the queue.
     - If the swapped right child is not `null`, add it to the queue.

3. **Reversing Nodes**:
   - The key operation is swapping the left and right children for each node during the traversal.
   - This inversion ensures that when we traverse all levels, the entire tree is inverted.

4. **Return**:
   - The tree is modified in place, so at the end of the traversal, the root node will point to the inverted binary tree.

#### Complexity:
   - **Time Complexity**: **O(n)**, where `n` is the number of nodes in the tree, as we visit each node once.
   - **Space Complexity**: **O(n)**, in the worst case when the tree is completely unbalanced, the queue will contain all nodes.

### Self Notes
To solve this problem using Iterative approach, we can use basic implementation of bfs with added code to reverse left & right nodes for each node. 


```
"""
    Iterative Solution

    using BFS for the iterative solution, hence using a queue
        Initialize the queue with root at start

    loop while queue is not empty
        pop the first value & reverse it's nodes
        if left exists - insert into queue
        if right exists - insert into queue

    return root at the end
"""
```

## Method 2 (Recursive approach)

To invert a binary tree using a **recursive approach**, we use **Depth-First Search (DFS)**. The goal is to swap the left and right children of each node as we recursively traverse the tree.

#### Steps:

1. **Base Case**:
   - If the current node is `null` (i.e., we've reached a leaf node’s child), return `null`.
   
2. **Recursive Inversion**:
   - Swap the left and right children of the current node.
   - Recursively call the function on the new left child (previously the right child).
   - Recursively call the function on the new right child (previously the left child).

3. **Return**:
   - After the left and right subtrees are inverted for the current node, return the node itself. The root node will ultimately point to the fully inverted binary tree.

#### Complexity:
   - **Time Complexity**: **O(n)**, where `n` is the number of nodes in the tree, since we visit each node exactly once.
   - **Space Complexity**: **O(h)**, where `h` is the height of the tree. In the worst case (completely unbalanced tree), the recursion stack will have a depth equal to the height of the tree. In the best case (balanced tree), the space complexity is O(log n).


### Self Notes
To solve this problem using Recursive approach, we can use basic implementation of dfs of recursion with added code to reverse left & right nodes for each node. 

```
"""
    Recursive Solution

    For every recursive function, there exists three mandatory things
        base condition -- checking if root is none
        recursive function call -- calling with both left & right node
        return statement - returning the input root node
    
    in addition to these, also implementing logic to reverse nodes
        left to right & right to left
"""
```
