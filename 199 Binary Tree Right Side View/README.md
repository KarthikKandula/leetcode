# 199. Binary Tree Right Side View

1 possible solutions for this problem  

## Method 1

To identify the last value at each level in a binary tree using BFS, follow these steps:

### Steps

1. **Initialize a Queue**:
   - Use a queue to manage nodes level by level, starting with the root node.

2. **Perform Level Order Traversal**:
   - Traverse the tree using BFS to process nodes level by level.
   - For each level, determine the number of nodes currently in the queue (this represents the number of nodes at that level).

3. **Collect the Last Value for Each Level**:
   - Use an inner loop to process all nodes at the current level:
     - Dequeue each node, collect its value, and add its children (left and right) to the queue.
   - After the inner loop completes, capture the value of the last node processed (which is the last value at that level).

4. **Store the Results**:
   - Append the last value of each level to an output array.

5. **Repeat Until All Levels Are Processed**:
   - Continue this process until the queue is empty, ensuring all levels of the tree are traversed.

6. **Return the Output Array**:
   - The output array will contain the last value from each level of the tree.

### Conclusion
This approach efficiently captures the last value at each level using BFS, with a time complexity of O(n), where `n` is the number of nodes in the tree.


### Self Notes
To solve this problem, we can use basic bfs tree traversal with some added code. the problem is to identify the last value by level in a binary tree, we use level order traversal's characteristics to our advantage, since in level order traversal, we go thru the tree based on levels, we create an inner loop after each level has completed so we get the last value in every level. append them to an output array & return it 


```
"""
   use basic level order traversal i.e, bfs to solve this problem
      the problem is to identify the last value in a level in a binary tree

   we use level order traversal's characteristics to our advantage
   since in level order traversal, we go thru the tree based on levels
   we create an inner loop after each level has completed so we go thru each level's values seperate

   take an empty output array
   take a queue -- used for bfs

   loop while queue is not empty
      get the queue's length at that point -- that is the no. of node's at that level
      create an inner loop & go thru the queue for queue's length from before
         pop from queue
         check if that node is the last at that level -- add to output array
         add left & right nodes to queue

   in the end, return output array
"""
```

