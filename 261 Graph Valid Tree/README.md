# 261. Graph Valid Tree

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to determine if a given graph (represented by nodes and edges) forms a valid tree. For a graph to be a valid tree, it must:
1. Be fully connected, meaning there are no isolated nodes.
2. Have no cycles, as trees do not contain cycles.

This problem can be approached using DFS to ensure each node is connected and that there are no cycles.

## Approach

### Key Idea
1. **Build a Graph Representation**: Use a hashmap to store each node and its list of connected nodes (edges).
2. **DFS to Detect Cycles and Check Connectivity**:
   - Use DFS to traverse the graph.
   - Track visited nodes to avoid reprocessing nodes and to detect cycles in an undirected graph.
   - Maintain a parent reference to avoid falsely detecting cycles due to undirected nature.

### Step-by-Step Solution

1. **Build the Graph**:
   - Create a hashmap where each node points to a list of its connected nodes.
   - Populate the hashmap based on the given edges.
   - Since this is an undirected graph, add each node on both sides of the edge.

2. **Define a Recursive DFS Helper Function**:
   - **Input**: Current node and the calling parent node.
   - **Base Case**:
     - If the node is already in the `visited` set, return `False` to indicate a cycle.
   - **Process the Current Node**:
     - Add the current node to the `visited` set to mark it as processed.
     - For each neighboring node:
       - If the neighboring node is the parent node, skip it to avoid retracing the same edge.
       - Recursively call the DFS helper function on the neighbor.
       - If any call returns `False`, propagate `False` to indicate that a cycle was detected.
   - Return `True` if all neighbors were processed without finding cycles.

3. **Perform DFS and Check Connectivity**:
   - Start DFS from any node (e.g., node `0`).
   - If the DFS function returns `False`, return `False`, indicating that the graph is not a valid tree.
   - After DFS completes, check if all nodes are visited.
     - If the size of the `visited` set equals the number of nodes, the graph is connected.
     - Otherwise, return `False`, as it indicates that not all nodes are connected.

4. **Return the Result**:
   - Return `True` if all nodes are connected and no cycles were found, otherwise return `False`.

### Summary
- **DFS Logic**: By using DFS with cycle detection and tracking of connected nodes, we ensure that the graph meets the requirements for a valid tree.
- **Efficiency**: Each node and edge is processed only once, making the approach efficient.
- **Output**: The function returns `True` if the graph is a valid tree; otherwise, it returns `False`.


### Self Notes

```
"""
  we can treat this problem as a graph traversal problem
    we can create a graph for every node & edge given in the problem
    the goal is to make sure we can take every node is connected & there are no cycles
    an added logic to notice is that this is an undirected edges between nodes
    so to counteract the undirectd nature, we add the nodes to each node on either side of the edge
    and record the previous node/calling parent node to ignore recursive call for that node

  create a hashmap with every node & populate the connections for each course
    since undirected, need to populate for either side of the edge
  create a set to take note of visited nodes already -- helps in detecting cycles

  create a helper function to implement recursively
    input is a node & calling parent node
    if node is in visited
      return False
    
    if reaches this point, it means this is a new node we're visiting & should be validated
    add node to visited
    loop thru all surrounding node's this node has & recusively call each course
      since this is an undirected graph, we need to skip the parent node
        compare if current node is parent, then skip it
      if any node returns false, return false for entire function
    
    if reaches this point, it means no course returned false
    return True

  in the end, return the return value of first func call & if length of visited is equal to the no of nodes
    to make sure there are no nodes that aren't connected to graph
"""
```

