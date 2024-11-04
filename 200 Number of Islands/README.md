# 200. Number of Islands

2 possible solutions for this problem  
- can be done iteratively and recursively

## Method 1 (Iterative Solution)

## Problem Intuition
In this problem, we are given a grid of `1`s (land) and `0`s (water). The task is to count the number of distinct islands, where an island is formed by connecting adjacent `1`s horizontally or vertically. An effective approach is to use Breadth-First Search (BFS) to explore each island fully as soon as we find an unvisited `1`.

## Approach

### Key Idea
1. **Use BFS** to explore and mark each island.
2. **Track Visited Locations**: Keep a record of visited `1`s to avoid recounting parts of the same island.
3. **Increment Island Count**: Each time we encounter an unvisited `1`, it represents a new island. We initiate a BFS from this point to mark the entire island as visited.

### Step-by-Step Solution

1. **Initialize Variables**:
   - `count` to store the number of islands.
   - `visited` set to keep track of locations that have already been explored.

2. **Loop Through the Grid**:
   - For each cell `(row, col)`, check if it contains a `1` and has not been visited.
   - If both conditions are met, it indicates the start of a new island. Increment the `count` and initiate a BFS to explore all connected `1`s.

3. **Perform BFS**:
   - Use a queue to process each location within the current island.
   - Add the starting position `(row, col)` to the queue and the `visited` set.
   - While the queue is not empty:
     - Dequeue the current position.
     - For each of the four adjacent directions (up, down, left, right):
       - Check if the adjacent cell is within bounds, contains a `1`, and has not been visited.
       - If valid, add it to the queue and mark it as visited.
   - This ensures that all `1`s connected to the initial position are visited and marked, avoiding redundant counts for the same island.

4. **Continue Until All Cells Are Processed**:
   - Repeat the process for each cell in the grid.
   - By the end of the grid traversal, `count` will hold the number of distinct islands.

5. **Return the Result**:
   - Return `count` as the total number of islands.

### Summary
- Each time we find an unvisited `1`, we increment `count` and perform a BFS to mark all connected `1`s as visited.
- This approach ensures each island is counted once, and we avoid double-counting any part of the same island.
- The use of a `visited` set and BFS efficiently tracks and explores each island.


### Self Notes

```
 """
  Iterative bfs solution

  we can solve this using Iterative BFS algorithm
    the entire logic of this problem is
    find the no of islands by knowing which locations have already been visited
      once a location with 1 is found, increment count
      add all adjacent 1's to visited -- count will not be increased for these
        if in future these are visited, we'll not increment count since they're in visited
      in essence increment count for the first 1 we hit & the rest will not be hit since they'll be visited by 1st 1
  
  after code runs for all locations, we'll have the count in output variable
"""
```

## Method 2 (Recursive Solution)

## Problem Intuition
In this problem, we are given a grid of `1`s (land) and `0`s (water). The task is to count the number of distinct islands, where an island is formed by connecting adjacent `1`s horizontally or vertically. We can use Depth-First Search (DFS) to explore each island fully once we encounter an unvisited `1`.

## Approach

### Key Idea
1. **Use DFS Recursively** to explore and mark each island.
2. **Track Visited Locations**: Use a `visited` set to keep track of the cells that have already been explored.
3. **Increment Island Count**: Every time we find an unvisited `1`, it represents a new island. We increment the `count` and use DFS to visit all the connected `1`s.

### Step-by-Step Solution

1. **Initialize Variables**:
   - `count` to store the number of islands.
   - `visited` set to track locations that have been visited.

2. **Loop Through the Grid**:
   - Use a nested loop to iterate over each cell `(row, col)` in the grid.
   - If the current cell contains a `1` and has not been visited:
     - Increment the `count`.
     - Call the recursive DFS function to mark the entire island as visited.

3. **Define the Recursive DFS Function**:
   - **Input**: `row` and `col` representing the current cell.
   - **Base Cases**:
     - If the current `row` or `col` is out of bounds, return immediately.
     - If the current cell is already in `visited`, return.
     - If the current cell does not contain a `1` (i.e., it is water), return.
   - **Mark the Cell as Visited**:
     - Add the current position `(row, col)` to the `visited` set.
   - **Recursive Calls**:
     - Make recursive calls for all four adjacent cells (up, down, left, right) to explore the entire island.

4. **Continue Until All Cells Are Processed**:
   - The nested loop ensures every cell in the grid is checked.
   - Each unvisited `1` triggers a DFS, marking all connected land cells, and the `count` is incremented for the new island.

5. **Return the Result**:
   - Once all cells are processed, return `count` as the total number of islands.

### Summary
- **DFS Logic**: When we encounter an unvisited `1`, we use DFS to visit all connected land cells, marking them as visited. This ensures that each island is counted only once.
- **Efficiency**: The use of a `visited` set and recursive DFS ensures an efficient exploration of the grid.

### Self Notes

```
"""
  Recursive solution

  we can solve this using Recursive DFS algorithm
    the entire logic of this problem is
    find the no of islands by knowing which locations have already been visited
      once a location with 1 is found, increment count
      add all adjacent 1's to visited -- count will not be increased for these
        if in future these are visited, we'll not increment count since they're in visited
      in essence increment count for the first 1 we hit & the rest will not be hit since they'll be visited by 1st 1
  
  loop thru each grid location in a nested loop
    to reduce no. of function calls
    check if location is 1 & if this isn't visited
      increment 

  create a helper recursive dfs function
    input is row & columns
    check if this row & col are out of bounds
      return
    check if this location is already visited
      return
    check if this location isn't an island
      return
    if reaches this point, means it's not visited & an island
    add to visited 
    make recursive calls for horizontal & vertical cells

  after code runs for all locations, we'll have the count in output variable
"""
```
