# 994. Rotting Oranges

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given a grid where:
- `0` represents an empty cell,
- `1` represents a fresh orange,
- `2` represents a rotten orange.

The task is to determine the minimum time required for all fresh oranges to become rotten by spreading the rot from adjacent rotten oranges each minute. A natural approach to solve this is using BFS, starting from all rotten oranges and spreading outwards.

## Approach

### Key Idea
1. **Use BFS from Rotten Oranges**: Instead of starting from each fresh orange, initiate BFS from all rotten oranges, allowing the rot to spread level by level.
2. **Track Fresh Oranges**: Maintain a count of fresh oranges, which will be decremented as they turn rotten. This helps to quickly determine if all oranges have rotted.

### Step-by-Step Solution

1. **Initialize Queue and Fresh Count**:
   - Create a `queue` to keep track of rotten oranges.
   - Traverse the grid to:
     - Add all initial rotten oranges (`2`) to the queue as starting points for BFS.
     - Count the number of fresh oranges (`1`).
   - If there are no fresh oranges, return `0` as the result immediately.

2. **Perform BFS Level by Level**:
   - Use BFS to process the rotten oranges in levels, representing each minute passing.
   - **Time Variable**: Initialize `time` as `0` to track the minutes.
   - While the `queue` is not empty and there are fresh oranges remaining:
     - For each orange in the current level:
       - Pop the current rotten orange from the `queue`.
       - For each of the four adjacent cells (up, down, left, right):
         - If an adjacent cell contains a fresh orange (`1`):
           - Mark it as rotten (`2`) and add it to the `queue`.
           - Decrement the fresh count.
     - After processing all oranges in the current level, increment the `time`.

3. **Check Remaining Fresh Oranges**:
   - If there are still fresh oranges left after the BFS completes, return `-1`, as not all oranges could be reached.
   - Otherwise, return `time`, which represents the minimum time required for all oranges to rot.

### Summary
- **BFS Logic**: Starting from all initially rotten oranges allows the rot to spread outwards in the minimum time.
- **Efficiency**: Each orange is processed only once, ensuring an efficient solution.
- **Output**: The `time` variable holds the minimum minutes required to rot all fresh oranges or `-1` if some fresh oranges remain unreachable.


### Self Notes

```
"""
   we can solve this problem using bfs graph traversal
      we can put a twist in the problem's approach
      instead of doing the operations from fresh oranges
      we can do the operations from rotten oranges & work backwards

   create a queue keep track of rotten oranges 
      insert all rotten oranges into queue in one loop thru entire grid
   variable to track fresh oranges
      count no of fresh oranges in one loop thru entire grid

   loop while queue is not empty & fresh count is greater than 0
      loop thru queue in levels -- to increment time value
         pop from queue
         insert all horizontal & vertical spots that are fresh oranges into queue
               update value to rotten
               decrement frsh count
      increment time after each level
   
   since we're returning the time, by the end of loop, time would be in variable
"""
```
