# 133. Clone Graph

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given a connected, undirected graph represented by a Node class. The task is to create a deep copy of the graph, where each node in the copy has the same neighbors as the original graph. Since each node's neighbors need to be copied and linked recursively, this is naturally suited for a DFS traversal approach.

## Approach

### Key Idea
1. **Use DFS** to traverse the graph and make copies of each node.
2. **Track Created Nodes**: Use a hashmap to map each original node to its corresponding copy, ensuring that each node is processed only once.

### Step-by-Step Solution

1. **Create a Hashmap**:
   - Use a `hashmap` to store the mapping of original nodes to their corresponding copies.
   - This helps to quickly check if a node has already been copied and to avoid processing the same node multiple times.

2. **Define a Recursive DFS Helper Function**:
   - **Input**: The current node being processed.
   - **Check If Node Exists in Hashmap**:
     - If the node already exists in the hashmap, return the copied node. This prevents redundant processing.
   - **Create a Copy of the Node**:
     - If the node is not in the hashmap, create a copy and insert it into the hashmap.
   - **Process Neighbors**:
     - Loop through each neighbor of the current node.
     - Recursively call the helper function for each neighbor.
     - Append the returned copy of the neighbor to the `neighbors` list of the current copy node.
   - **Return the Copy Node**:
     - Once all neighbors are processed, return the copy of the current node.

3. **Initiate DFS from the Starting Node**:
   - If the input node is `null`, return `null`.
   - Otherwise, call the DFS helper function on the input node and return the result.

### Summary
- **DFS Logic**: We use DFS to traverse each node, creating a copy and establishing the connections recursively.
- **Hashmap**: The hashmap ensures that each node is copied only once and provides efficient lookups.
- **Output**: By the end of the recursion, all nodes will have been cloned, and their connections will be correctly established.


### Self Notes

```
"""
   we can solve this problem using dfs graph traversal
      since we need to create a copy for each node & assign neighbors to each one, this is a recursive problem
      the basic idea is to create a copy & then call the recursive function for each neighbor to do the same
   
   create a hashmap to track old nodes for new nodes

   create a helper function that implements recursive dfs
      input is the node currently processed
      check if it already exists in hashmap
         if it does, return the new node
      if the node doesnt exist in the hashmap
      create a copy for the node
      insert it into the hashmap
         assign value to old node
      loop for each neighbor of old node
         recursively call for each node
         append the returned node (value) to copy node's neighbors array
      return copy node  

   once all recursive functions are created, each & every node should be created & connections established.
"""
```
