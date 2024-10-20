# 297. Serialize and Deserialize Binary Tree

1 possible solution for this problem  

## Method 1

## Solution Approach: Recursive DFS for Serializing and Deserializing a Binary Tree

To serialize and deserialize a binary tree using recursive DFS pre-order traversal, follow these steps:

### Serialization

1. **Use Recursive Pre-Order Traversal**:
   - Traverse the tree in a pre-order manner (root -> left -> right) to capture each node’s value.
   - Use recursion to easily access and append values at each node.

2. **Build the Serialized String**:
   - If a `None` (null) node is encountered, append `"N"` to the array.
   - If a valid node value is encountered, append the value to the array.
   - Recursively call the function for the left and right subtrees to continue the traversal.
   - After all nodes are processed, join the array elements with a `,` delimiter to form the final serialized string.

3. **Return the Serialized String**:
   - The result is a single string representing the serialized tree.

### Deserialization

1. **Split the Serialized Data**:
   - Split the input string using the `,` delimiter to create an array of values.

2. **Use Recursive Pre-Order Traversal to Rebuild the Tree**:
   - Create a `count` variable to keep track of the current index in the array.
   - Define a recursive function that checks the current value:
     - If the value is `"N"`, return `None` as it represents a null node.
     - If the value is valid, create a new node with that value.
   - Recursively call the function to build the left and right subtrees for the node.

3. **Return the Reconstructed Tree**:
   - The main function returns the root node created from the recursive calls, representing the deserialized tree.

### Conclusion

This approach efficiently serializes and deserializes a binary tree using recursive DFS, ensuring a time complexity of O(n), where `n` is the number of nodes in the tree.


### Self Notes
To solve this problem, we use recursive dfs pre-order traversal with added logic & code.

serialize ops
the solution is going to be recursive since we need to get values at each node & append to array. hence recursion is the simplest way to go. if found a None node append N to array, if found value append to array & recursively call for left & right subtrees. in the end join array values with , delimiter & make it a string

deserialize ops
the solution is going to be recursive since we need to build nodes at each node & that need to happend for it's children & it's children (if exists). hence recursion is the simplest way to go. split input data by , so that values are in array, create a count variable that always points to the current value. in the recursive function, check if current value is N, which means None, return it. create a node if a value exists & recursively call to build left & right subtrees. return created node in the end. the main functions return value is going to the node returned for root call.


```
serialize
"""
   use dfs pre-order traversal to serialize the tree
      indicate null nodes by N
   
   create an array to store node values -- makes it easy for append ops
   after implementing dfs pre-order traversal recursively

   convert array into string with , delimiters before returning
"""

deserialize
"""
   use dfs pre-order traversal to deserialize the tree
   
   create an array to store node values -- makes it easy to access value
      split input string by ,'s
   create a count value that indicates current position in the above array

   create a helper function to implement dfs recursively
      if current position in array is N
         increment count value -- for future ops
         return None
      create a node with current position's value
         increment count value -- for future ops
      recursive call for left subtree
      recursive call for right subtree

      return node at the end

   return the node that is returned for first function call -- that is the root node
"""
```

