# 286. Walls and Gates

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to fill each empty room (`INF`) in a grid with the distance to its nearest gate (`0`). We can optimize the process by starting from all the gates and performing a multi-source BFS to propagate distances to the empty rooms. This way, we efficiently calculate the shortest distance for each room.

## Approach

### Key Idea
1. **Use BFS from the Gates**: Instead of starting from each empty room, start from the gates and work outwards. This ensures that we fill the shortest distance for each room efficiently.
2. **Track Visited Locations**: Since we're updating the grid in-place, we don't need an explicit visited set; we can use the distance values in the grid to check if a room has been visited.

### Step-by-Step Solution

1. **Initialize a Queue**:
   - Create a `queue` to keep track of gates and their distances.
   - Loop through the entire grid to find all the gates (`0`) and add them to the `queue` as starting points for BFS.

2. **Perform BFS Level by Level**:
   - Use BFS to process the nodes in levels, ensuring that all nodes at the same distance from a gate are processed together.
   - **Distance Value**: Start with a distance of `0` and increment it as we move further from the gates.
   - While the `queue` is not empty:
     - For each node in the current level:
       - Pop the node from the `queue`.
       - Update the corresponding room with the current distance.
       - Check all four adjacent directions (up, down, left, right):
         - If an adjacent node is within bounds and is an empty room (`INF`), update it and add it to the `queue`.
     - Increment the distance value after processing each level.

3. **In-Place Updates**:
   - Since the values in the grid are updated in-place, there is no need to return anything.

### Summary
- **BFS Logic**: By using BFS from all gates simultaneously, we ensure that the shortest distances are calculated efficiently.
- **Efficiency**: The approach avoids unnecessary recalculations and ensures each room is visited only once.
- **Output**: The grid is updated in-place with the shortest distances to the nearest gate.


### Self Notes

```
"""
   we can solve this problem using dfs graph traversal 
      we can put a twist in the problem's approach
         instead of doing the operations from empty rooms, we can do the operations from gates & work backwards
   
   create a queue & set to take note of visited values

   loop thru the entire input to find gates & insert into queue

   now loop while queue is not empty
      loop thru the queue in levels -- to increment distance value
         pop from queue
         update that location with distance 
         insert all the horizontal & vertical nodes that are empty rooms into queue
      increment distance value after each level
   
   since we're update values in-place, no need to return
"""
```
