# 104. Maximum Depth of Binary Tree

2 possible solution for this problem  
- Iterative & Recursive approach

## Method 1 (Iterative approach)

Follow these steps to solve the problem using an iterative DFS approach:

1. **Initialize a Stack**: Start with a stack containing the root node and its depth (e.g., `[node, depth]` where `depth` starts at 1).
   
2. **Iterate Through the Stack**:
   - Pop an element from the stack to retrieve the current node and its depth.
   - Update the maximum depth if the current depth is greater than the previous maximum.

3. **Add Child Nodes to the Stack**:
   - For each child node of the current node, add it to the stack in the format `[child_node, depth + 1]` to update the depth for each child correctly.

4. **Return the Maximum Depth**: Once the stack is empty, return the maximum depth encountered during the traversal.

### Self Notes
To solve this problem using Iterative approach, we can use basic implementation of DFS with added code to keep track of the depth at each particular node. insert into stack in this format - [node, depth until that node], while adding nodes to the stack, add in this format but add 1 that keeps the depth updated for each node. In the end return max depth that was ever encountered. 

```
"""
   Iterative Solution

   we can solve this problem in iterative approach using basic DFS tree traversal
      with slight change on adding nodes to stack
   
   add nodes to stack in this format - [node, depth until that node]
      this is to have an idea of the depth for each node

   loop while stack is not empty
      get latest value from stack
      get max value of depth from the popped node's tempdepth
      append popped node's left & right nodes to stack for further processing
   
   in the end max depth will be stored in depth variable, return at end
"""
```

## Method 2 (Recursive approach)

To solve the problem using a recursive DFS approach, follow these steps:

1. **Define the Recursive Function**: Create a function that takes the current node as input and returns the depth of the tree rooted at that node.

2. **Base Case**: 
   - If the current node is `null`, return a depth of 0.

3. **Recursive Calls**: 
   - Recursively call the function for the left child and the right child to obtain their respective depths.

4. **Calculate Maximum Depth**:
   - For the current node, compute the maximum depth as `max(left_depth, right_depth) + 1`, where `left_depth` and `right_depth` are the depths of the left and right subtrees.

5. **Return the Depth**: Return the calculated maximum depth for the current node.

6. **Initial Call**: Start the recursion with the root node to get the maximum depth of the entire tree.

### Self Notes
To solve this problem using Recursive approach, we can use basic implementation of DFS with added code to consider the depth at each particular node. we'll make slight adjustment to the way we return values, instead of returning nodes, we'll return the depth at each node. and for each node, we'll get the depth of left & right subtrees, now return the max of left, right & add 1 to this to account for the current node.  

```
"""
   Recursive Solution

   we can solve this problem in recursive approach using basic DFS tree traversal
      with slight change on return values
   
   we don't return the root node itself, instead
      we return the depth at that particular node
         add 1 to include the current node as well along with the max of left & right nodes
"""
```
