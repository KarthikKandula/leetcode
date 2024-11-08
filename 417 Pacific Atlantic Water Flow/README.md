# 417. Pacific Atlantic Water Flow

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given an `m x n` matrix representing the heights of a grid. The task is to find all positions from which water can flow to both the Pacific and Atlantic oceans. Cells connected horizontally or vertically to the ocean borders can potentially reach the ocean. Instead of checking every cell, we can simplify the problem by only starting DFS from the borders.

## Approach

### Key Idea
1. **Use DFS from Border Cells**: Perform DFS starting from cells on the borders of the matrix, as these cells are accessible directly to either the Pacific or Atlantic oceans.
2. **Track Reachable Cells**: Use two sets to track positions reachable from each ocean:
   - `pacific` for cells that can reach the Pacific Ocean (top and left borders).
   - `atlantic` for cells that can reach the Atlantic Ocean (bottom and right borders).
3. **Intersection of Reachable Sets**: The cells that appear in both sets (`pacific` and `atlantic`) can flow to both oceans and are the required result.

### Step-by-Step Solution

1. **Initialize Data Structures**:
   - Create two sets, `pacific` and `atlantic`, to store cells that can reach each respective ocean.

2. **Perform DFS from Border Cells**:
   - For the **Pacific Ocean**:
     - Start DFS from all cells in the top row and the left column.
   - For the **Atlantic Ocean**:
     - Start DFS from all cells in the bottom row and the right column.
   - The DFS function should:
     - Add each cell to the respective ocean's set if it can reach that ocean.
     - Explore neighboring cells (up, down, left, right) that have equal or greater height to allow water flow.

3. **Define DFS Helper Function**:
   - **Input**: Current cell `(row, col)` and the ocean-specific set (`pacific` or `atlantic`).
   - **Base Cases**:
     - If the cell is already in the respective ocean set, return to avoid redundant processing.
     - If the cell is out of bounds, return.
   - **Process the Current Cell**:
     - Add the cell to the ocean set.
   - **Recursive Calls**:
     - For each neighboring cell that is within bounds and has an equal or higher height, call DFS recursively.

4. **Find the Intersection**:
   - After both DFS operations complete, the intersection of `pacific` and `atlantic` sets represents cells that can flow to both oceans.
   - Convert the intersection to a list of coordinates for the final result.

5. **Return the Result**:
   - Return the list of cells that can reach both oceans.

### Summary
- **DFS Logic**: Starting from the ocean borders allows efficient identification of reachable cells, reducing redundant calculations.
- **Efficiency**: Each cell is processed only once per ocean, resulting in an optimized solution.
- **Output**: The intersection of `pacific` and `atlantic` sets provides the final list of cells that can flow to both oceans.


### Self Notes

```
"""
   First approach
      Performing DFS from each position & checking if there is a path to either ocean
      Time complexity becomes O(m x n)^2
   
   we can solve the problem using dfs graph traversal
      instead of performing dfs from each position & checking if there is a path to either ocean
      we can perform dfs on border positions since they're accessible to atleast once ocean
      add positions accessible to oceans in their respective sets - pacific & atlantic
      Compare both sets for common tuples -> these are the final result requested
"""
```
