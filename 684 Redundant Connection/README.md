# 684. Redundant Connection

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given an undirected graph represented by a list of edges. The task is to find the first edge that, when added, forms a cycle in the graph. This edge is considered the "redundant connection" since removing it would make the graph a tree (connected and acyclic). The Union-Find (Disjoint Set Union) algorithm is well-suited for detecting cycles in an undirected graph.

## Approach

### Key Idea
1. **Use Union-Find for Cycle Detection**: 
   - The Union-Find algorithm helps in determining if adding an edge would connect two nodes that are already in the same component (i.e., form a cycle).
2. **Track Parent and Rank**:
   - Use two arrays, `parent` and `rank`, for Union-Find operations:
     - `parent` array tracks the root parent of each node.
     - `rank` array keeps trees balanced by storing the size of each component.

### Step-by-Step Solution

1. **Initialize Union-Find Structures**:
   - Create a `parent` array where each node is its own parent initially, indicating separate components.
   - Create a `rank` array where each node has an initial rank of 1, representing the size of the component.

2. **Define the Find Function with Path Compression**:
   - **Input**: Node `x`.
   - **Process**: Recursively find the root parent of `x` and apply path compression by updating `x` to point directly to the root.
   - **Return**: The root of `x`.

3. **Define the Union Function with Union by Rank**:
   - **Input**: Nodes `x` and `y`.
   - **Process**:
     - Find the root parents of `x` and `y` using the `find` function.
     - If they share the same root, a cycle is detected, and the function returns `False`.
     - Otherwise, connect the smaller tree to the larger tree:
       - If `rank[x] > rank[y]`, make `y`'s root point to `x`.
       - If `rank[y] > rank[x]`, make `x`'s root point to `y`.
       - If `rank[x] == rank[y]`, arbitrarily make one root point to the other and increment its rank.
     - Return `True` to indicate successful union without a cycle.

4. **Process Each Edge**:
   - Loop through each edge in the list.
   - For each edge, use the `union` function to connect the two nodes.
   - If `union` returns `False`, it means the edge forms a cycle and is the redundant connection. Return this edge immediately.

5. **Return the Result**:
   - The first cycle-causing edge returned by `union` is the redundant connection.

### Summary
- **Union-Find Logic**: Using Union-Find with path compression and union by rank allows efficient cycle detection and minimizes tree height, optimizing for future union and find operations.
- **Efficiency**: Each edge is processed only once, making the approach efficient for detecting cycles in the graph.
- **Output**: The function returns the first edge that forms a cycle, which is the redundant connection.


### Self Notes

```
"""
   we can treat this as a cycle detection problem in an undirected graph
      given a list of edges, we aim to identify the redundant edge that forms a cycle
      the goal is to find the first edge that creates a cycle when added to the graph
   
   create two arrays, parent and rank, for Union-Find (Disjoint Set Union) operations
      parent array tracks the root parent of each node, initialized with each node as its own parent
      rank array tracks the size of each tree, initialized with rank 1 for each node

   create a helper function `find` to locate the root of a node
      this function implements path compression
      by updating each node's parent to point directly to the root, it optimizes future calls

   create a helper function `union` to connect two nodes
      this function implements union by rank to keep trees balanced
      it returns False if the nodes are already connected (indicating a cycle) and True otherwise
   
   loop through each edge in the input
      for each edge, attempt to union the two nodes
      if union fails, it means the edge creates a cycle, so return this edge
   
   by the end of the loop, the first cycle-causing edge is returned as the redundant connection
"""
```
