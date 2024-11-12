# 1584. Min Cost to Connect All Points

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given a set of points on a 2D plane and need to connect all points with the minimum cost, where the cost to connect two points `(x1, y1)` and `(x2, y2)` is the Manhattan distance `|x1 - x2| + |y1 - y2|`. This problem can be visualized as finding the Minimum Spanning Tree (MST) of a fully connected graph, where each point is a node, and edges represent distances between points. We use Prim's Algorithm to efficiently construct the MST.

## Approach

### Key Idea
1. **Use Prim's Algorithm for MST**:
   - Prim's Algorithm grows the MST by adding the minimum-cost edge from the visited set to any unvisited node.
2. **Construct an Adjacency List**:
   - Represent the graph using an adjacency list where each point is connected to every other point with the edge cost equal to the Manhattan distance.

### Step-by-Step Solution

1. **Build the Adjacency List**:
   - Create an adjacency list `adjList`, where each node (point) maps to a list of neighboring nodes with their respective distances.
   - For each pair of points `(i, j)`, calculate the Manhattan distance and store `[cost, j]` in the adjacency list for `i` and `[cost, i]` in the list for `j`.

2. **Initialize Prim's Algorithm Structures**:
   - Initialize `result` to store the minimum cost, starting at `0`.
   - Initialize a `visited` set to keep track of nodes already included in the MST.
   - Use a `minHeap` initialized with `[0, 0]` (distance `0` to node `0`) to kick off the algorithm by starting at node `0`.

3. **Run Prim's Algorithm**:
   - While the length of `visited` is less than the number of points:
     - Pop the smallest element from `minHeap`, giving the node with the minimum connection cost.
     - If the node is already in `visited`, skip to the next iteration.
     - If the node is not in `visited`:
       - Add the node to `visited`.
       - Add the connection cost to `result`.
     - For each neighbor of the current node, add it to `minHeap` with its cost if it has not been visited. This ensures we only consider edges from nodes already in the MST to nodes not yet visited.

4. **Return the Result**:
   - Once all nodes have been visited, `result` contains the minimum cost to connect all points.

### Summary
- **Prim's Algorithm Logic**: Prim’s Algorithm ensures the MST is constructed by continuously adding the minimum-cost edge to the visited set.
- **Efficiency**: The adjacency list and min-heap provide efficient lookups and insertions, minimizing redundant edge checks.
- **Output**: The function returns the minimum cost required to connect all points.


### Self Notes

```
"""
   we treat this as a graph problem where each point is a node
      we use Prim's algorithm to solve this problem
      to solve using Prim's algorithm we need an adjacency list
      so we build an adjacency list where we calculate the distance between each node
      also, we name the nodes based on their indexes in input points.
   
   create a hashmap for adjacency list
      populate adjacency list by calcuating distance between two points -- do this between all points in list
      saved in format [cost, node]
   
   take a result variable -- initialized to 0
   take a visited set
   take a minHeap
      initialize it to [0, 0] to kickoff the algorithm
      this means we're visiting node 0 in the first iteration which will add all node 0's neighbors to the minheap
   
   implementing prim's algorithm
      loop while visited length is less than num of points -- aka not all nodes have been visited
      pop from minHeap -- get's the node with smallest distance
      check if it's already in visited
         if yes, skip iteration
      if not, this is a new node & we need to make the connection
      add to visited
      add cost to result variable
      loop thru this node's neighbors
         add all nodes to minHeap if they're not in visited
   
   once all nodes have been visisted, result is in the variable, return it
"""
```
