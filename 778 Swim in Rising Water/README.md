# 778. Swim in Rising Water

1 possible solution for this problem  

learn djisktra's algo later

## Method 1

## Problem Intuition
We are given an `n x n` grid where the value at each cell represents the time at which the water rises to that level. The task is to determine the minimum time required to swim from the top-left corner `(0, 0)` to the bottom-right corner `(n-1, n-1)` while ensuring that at no point does the swimmer go through a cell where the water level hasn't risen yet. This can be solved as a shortest path problem in a weighted grid, making Dijkstra's Algorithm an ideal choice.

## Approach

### Key Idea
1. **Use Dijkstra's Algorithm for Shortest Path**:
   - Maintain a priority queue (min-heap) to process nodes by their minimum time to reach.
   - Track visited nodes to avoid revisiting and redundant processing.
2. **Minimize Time to Reach Destination**:
   - Use the heap to prioritize paths with the least time and process neighbors.

### Step-by-Step Solution

1. **Initialize Structures**:
   - Create a `visited` set to track processed nodes.
   - Create a min-heap (priority queue) to process cells in the format `(time, row, col)`, where `time` is the maximum water level encountered on the path to that cell.
   - Add the starting cell `(grid[0][0], 0, 0)` to the heap.

2. **Dijkstra's Algorithm**:
   - While the heap is not empty:
     - Pop the smallest element from the heap, giving the cell `(time, row, col)` with the minimum time.
     - If the cell is `(n-1, n-1)` (bottom-right corner), return `time` as the result since it represents the minimum time to reach the destination.
     - If the cell is already in the `visited` set, skip it.
     - Mark the cell as visited.
     - Explore its neighbors (up, down, left, right):
       - For each neighbor:
         - Check if the neighbor is within bounds and not in the `visited` set.
         - Add the neighbor to the heap with the updated `time`:
           - The updated `time` is the maximum of the current `time` and the water level at the neighbor (`grid[newRow][newCol]`).

3. **Guaranteed Solution**:
   - Since a solution is guaranteed by the problem constraints, the loop will always return a value when `(n-1, n-1)` is reached.

### Summary
- **Dijkstra's Algorithm Logic**: The algorithm ensures that the first path to reach the destination `(n-1, n-1)` is the shortest (minimum time), as the priority queue processes nodes in ascending order of time.
- **Efficiency**: The min-heap and visited set ensure that each node is processed only once, making the solution efficient.
- **Output**: The function returns the minimum time required to swim from the top-left to the bottom-right corner.

### Self Notes

```
"""
   Djikstra's algorithm

   use Djikstra's algorithm to solve the problem
      the objective is to find the least amount of time until you reach the bottom right square (n-1,n-1)
      since it's an algo to find the shortest path, djistra's algorithm is the best

   create a set to record visited nodes -- so not to visit nodes again
   create a heap -- format: (time, row, col) -- time is the cumulative time taken to reach any particular spot
      populate heap with first value to kickstart the algo

   loop while minheap has values
      pop from heap
      check if the popped location is (n-1,n-1)
         we reached the destination, return time value of popped element
         since djikstra's algo is shortest path algo
            the first path to reach node (n-1,n-1) is the shortest path, hence we can return the value
         if this location is already in visited -- skip it
         now loop for horizontal & vertical directions
            check if the direction is out of bounds or in visited set
               if not, add to heap
   
   since a solution is guaranteed, the return function will return a value
"""
```
