# 695. Max Area of Island

2 possible solutions for this problem  
- can be done iteratively and recursively

## Method 1 (Iterative Solution)

## Problem Intuition
We are given a grid of `1`s (land) and `0`s (water) and need to find the maximum area of any island, where an island is formed by connecting adjacent `1`s horizontally or vertically. We can solve this efficiently using an iterative Breadth-First Search (BFS) approach.

## Approach

### Key Idea
1. **Use BFS** to explore each island and calculate its area.
2. **Track Visited Locations**: Use a `visited` set to keep track of cells that have already been processed.
3. **Calculate Island Area**: Use a local variable to keep track of the area of the current island. Increment this variable for every connected `1` encountered.

### Step-by-Step Solution

1. **Initialize Variables**:
   - `max_area` to store the maximum area encountered.
   - `visited` set to keep track of all visited locations.

2. **Loop Through the Grid**:
   - Use a nested loop to iterate through each cell `(row, col)` in the grid.
   - If the current cell contains a `1` and has not been visited, perform a BFS to calculate the area of the island.

3. **Perform BFS**:
   - Use a queue to keep track of cells to be processed.
   - Add the starting cell `(row, col)` to the queue and mark it as visited.
   - Initialize `area` as `0` to track the size of the current island.
   - While the queue is not empty:
     - Dequeue the current cell.
     - Increment `area` by `1`.
     - Check all four adjacent cells (up, down, left, right):
       - If an adjacent cell is within bounds, contains a `1`, and has not been visited:
         - Add the cell to the queue and mark it as visited.
   - After the BFS completes, update `max_area` with the maximum of `max_area` and `area`.

4. **Continue Until All Cells Are Processed**:
   - Repeat the process for each unvisited `1` in the grid.
   - By the end of the grid traversal, `max_area` will hold the size of the largest island.

5. **Return the Result**:
   - Return `max_area` as the final output.

### Summary
- **BFS Logic**: We use BFS to explore each island fully and calculate its area. The `max_area` is updated after processing each island.
- **Efficiency**: The use of a `visited` set ensures that each cell is processed only once, making the approach efficient.

### Self Notes

```
"""
  Iterative BFS solution
    we can solve this using Iterative BFS algorithm
    the entire logic of this problem is
    find the max area of islands by knowing which locations have already been visited
    know the area of each island by creating a local variable & increment it everytime 1 is found adjacent
    replace output value with max of each area of an island

  after code runs for all locations, we'll have the count in output variable
"""
```

## Method 2 (Recursive Solution)

## Problem Intuition
We need to determine the maximum area of any island in a grid of `1`s (land) and `0`s (water). An island is formed by connecting adjacent `1`s either horizontally or vertically. We can use a recursive Depth-First Search (DFS) to explore each island and calculate its area.

## Approach

### Key Idea
1. **Use Recursive DFS** to explore each island and calculate its area.
2. **Track Visited Locations**: Use a `visited` set to ensure each land cell (`1`) is processed only once.
3. **Calculate Island Area**: Use a recursive DFS function to explore all connected `1`s and return the area.

### Step-by-Step Solution

1. **Initialize Variables**:
   - `max_area` to store the maximum area of an island encountered.
   - `visited` set to keep track of all cells that have already been explored.

2. **Loop Through the Grid**:
   - Use a nested loop to iterate through each cell `(row, col)` in the grid.
   - If the current cell contains a `1` and has not been visited:
     - Call the recursive DFS function to calculate the area of the island.
     - Update `max_area` with the maximum of `max_area` and the area returned by the DFS.

3. **Define the Recursive DFS Function**:
   - **Input**: `row` and `col` representing the current cell.
   - **Base Cases**:
     - If the current `row` or `col` is out of bounds, return `0`.
     - If the current cell is already in `visited`, return `0`.
     - If the current cell does not contain a `1` (i.e., it is water), return `0`.
   - **Process the Current Cell**:
     - Mark the cell `(row, col)` as visited.
   - **Recursive Calls**:
     - Make recursive DFS calls for all four adjacent cells (up, down, left, right) to explore the entire island.
   - **Return the Area**:
     - Return `1` (for the current cell) plus the sum of the areas from all recursive calls.

4. **Continue Until All Cells Are Processed**:
   - The nested loop ensures that every cell in the grid is checked.
   - The DFS function fully explores each island and returns its area, updating `max_area` as needed.

5. **Return the Result**:
   - Return `max_area` as the largest island area found.

### Summary
- **DFS Logic**: The recursive DFS explores each island fully and calculates the area by summing up all connected `1`s.
- **Efficiency**: Each cell is processed only once, and the use of recursion makes the area calculation straightforward.

### Self Notes

```
"""
  Recursive DFS solution

  we can solve this using Recursive DFS algorithm
  
  loop thru each grid location in a nested loop
    to reduce no. of function calls
    check if location is 1 & if this isn't visited
    once a function returns, update max value to output

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

    in the end return sum of all recursive calls along with 1 -- to account for current location

  after code runs for all locations, we'll have the count in output variable
"""
```
