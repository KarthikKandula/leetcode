# 787. Cheapest Flights Within K Stops

1 possible solution for this problem  

learn djisktra's algo later

## Method 1

## Problem Intuition
We are given a set of flights with prices between cities (nodes) and need to find the cheapest way to travel from a source city to a destination city, with a constraint of making at most `K` stops. Since we are asked to find the minimum cost with limited transitions, the Bellman-Ford algorithm is a suitable choice because it iterates over edges, progressively finding the shortest path up to a given number of relaxations (`K + 1`).

## Approach

### Key Idea
1. **Use Bellman-Ford for Limited Relaxations**:
   - Bellman-Ford finds the shortest path with edge relaxation. By iterating up to `K + 1` times, we limit the path length to `K` stops.
2. **Track Minimum Costs per Iteration**:
   - Use an array to store the minimum cost to reach each node, updated progressively within each iteration.

### Step-by-Step Solution

1. **Initialize the Cost Array**:
   - Create an array `cost` of size equal to the number of cities, initialized with `inf` to represent unreachable nodes.
   - Set the cost of the `source` node to `0` as it’s the starting point.

2. **Iterate for `K + 1` Times (Relax Edges)**:
   - For each iteration from `0` to `K`:
     - Create a temporary array `tempCost` as a copy of `cost` to store intermediate values. This allows updating costs without interference within the current iteration.
     - For each flight `(u, v, price)` in the input:
       - If `cost[u]` is `inf`, skip this flight, as it means `u` is currently unreachable.
       - If `cost[u] + price < tempCost[v]`, update `tempCost[v]` to `cost[u] + price`, indicating a cheaper way to reach `v`.
     - After processing all flights, assign `tempCost` to `cost` to carry the latest minimum costs into the next iteration.

3. **Return the Result**:
   - After `K + 1` iterations, check `cost[dest]`:
     - If it is still `inf`, return `-1`, indicating that the destination is unreachable within `K` stops.
     - Otherwise, return `cost[dest]`, representing the minimum cost to reach the destination within the allowed stops.

### Summary
- **Bellman-Ford Logic**: The algorithm iteratively relaxes edges to progressively find the minimum cost path within `K + 1` relaxations.
- **Efficiency**: By only iterating `K + 1` times and using a temporary array to avoid interference within iterations, we efficiently track the minimum costs up to `K` stops.
- **Output**: The function returns the minimum cost to reach the destination within `K` stops, or `-1` if unreachable.


### Self Notes

```
"""
   using Bellman-Ford Algo

   this is a graph-traversal problem which will be better to use Bellman-Ford
      Bellman-Ford is best to find the shortest path to every node
      this will be achieved by only looping thru the input/graph k + 1 times -- derived from problem desc
      if the value isn't set in k + 1 loops, it means no path exists, so we return -1

   create an array with inf values for each node
      replace source node's to 0 -- since starting there
   
   loop thru the input k + 1 times
      before each loop, create a temp array -- copy of above array
         so it doesn't interfere with the value updates done in current loop
      while looking at each node, if any node's value in inf
         it means it hasn't yet been looked at, skip that value
      if at any point the node's source value + price < destination value from temparray
         replace value in temparray
      assign temparray values to actual array
   
   in the end after loop is done, return values based on problem condition
"""
```
