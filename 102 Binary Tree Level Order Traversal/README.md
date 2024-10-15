# 102. Binary Tree Level Order Traversal

1 possible solutions for this problem  

## Method 1

To identify and collect values by level in a binary tree using BFS, follow these steps:

### Steps

1. **Initialize a Queue**:
   - Use a queue to manage nodes as they are processed, starting with the root node.

2. **Perform Level Order Traversal**:
   - Traverse the tree level by level using the queue.
   - For each level, determine the number of nodes currently in the queue (this represents the number of nodes in that level).

3. **Collect Values for Each Level**:
   - Create an inner loop that processes all nodes at the current level.
   - Dequeue each node, collect its value, and add its children (left and right) to the queue.

4. **Store the Results**:
   - After processing each level, store the collected values separately, representing each level of the tree.

5. **Repeat Until All Levels Are Processed**:
   - Continue this process until the queue is empty, ensuring all levels of the tree are traversed.

### Conclusion
This approach efficiently captures the values in each level of a binary tree using BFS, with a time complexity of O(n), where `n` is the number of nodes in the tree.

### Self Notes
To solve this problem, we can use basic bfs tree traversal with some added code. the problem is to identify values by level in a binary tree, we use level order traversal's characteristics to our advantage, since in level order traversal, we go thru the tree based on levels, we create an inner loop after each level has completed so we get each level's values seperate. 

```
"""
   we can use basic level order traversal i.e, bfs to solve this problem
      the problem is to identify values by level in a binary tree

   we use level order traversal's characteristics to our advantage
      since in level order traversal, we go thru the tree based on levels
      we create an inner loop after each level has completed so we get each level's values seperate

   take an empty output array
   take a queue -- used for bfs

   loop while queue is not empty
      create an empty temp array for that level
      get the queue's length at that point -- that is the no. of node's at that level
      create an inner loop & go thru the queue for queue's length from before
         pop from queue
         add value to level array
         add left & right nodes to queue
      after inner loop has exited, add level to output -- we got all the values at that level

   in the end, return output array
"""
```

