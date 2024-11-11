# 323. Number of Connected Components in an Undirected Graph

1 possible solution for this problem  

need to learn iterative solution

## Method 1

## Problem Intuition
We are given a set of nodes and undirected edges, and the task is to find the number of connected components (subgraphs) in the graph. Each connected component consists of nodes that are directly or indirectly connected. We can approach this problem using DFS to traverse each component and track visited nodes to avoid recounting.

## Approach

### Key Idea
1. **Build a Graph Representation**: Use a hashmap to store each node and its list of connected nodes (edges).
2. **Track Connected Components Using DFS**:
   - Use DFS to traverse each component starting from any unvisited node, marking all reachable nodes as visited.
   - Each time a DFS starts from an unvisited node, it represents a new connected component.

### Step-by-Step Solution

1. **Build the Graph**:
   - Create a hashmap where each node points to a list of its connected nodes.
   - Populate the hashmap based on the given edges.
   - Since this is an undirected graph, add each node on both sides of each edge.

2. **Define a Recursive DFS Helper Function**:
   - **Input**: Current node.
   - **Process the Current Node**:
     - Add the node to the `visited` set to mark it as processed.
     - For each neighbor of the current node:
       - If the neighbor is not in `visited`, recursively call the DFS function on it to mark all connected nodes as visited.

3. **Count Connected Components**:
   - Initialize a `count` variable to `0`.
   - Loop through each node from `0` to `n-1`:
     - If the node is not in `visited`, it marks the start of a new connected component.
     - Call the DFS function on the node to mark all reachable nodes in this component as visited.
     - Increment `count` to reflect the new component.

4. **Return the Result**:
   - Return `count`, which holds the total number of connected components in the graph.

### Summary
- **DFS Logic**: Each DFS traversal starting from an unvisited node captures all nodes in a connected component, allowing us to accurately count the components.
- **Efficiency**: Each node and edge is processed only once, making the approach efficient.
- **Output**: The function returns the number of connected components in the undirected graph.


### Self Notes

```
"""
  we can treat this as a graph traversal problem
    we can create a graph for every node & edge given in the problem
    the goal is to get the no. of connected graphs in the input
    an added logic to notice is that this is an undirected edges between nodes
    so to counteract the undirectd nature, we add the nodes to each node on either side of the edge
    the entire logic is based out of the visited set
      checking if a node is in visited set 
      incrementing result variable only if it isn't

  create a hashmap with every node & populate the connections for each course
    since undirected, need to populate for either side of the edge
  create a set to take note of visited nodes already -- helps in detecting cycles

  create a helper function to implement recursively
    input is a node

    loop thru all surrounding node's this node has
      check if the current neighbor node is in visited
        if it isn't, do below
        add node to visited
        recusively call each neighbor
  
  loop thru range(n) to call recursive function for all nodes
    check if the current node is in visited
      if it isn't, do below
      add node to visited
      recusively call each neighbor
      increment result variable
  
  by the time all nodes have been called, result is in the variable
"""
```

