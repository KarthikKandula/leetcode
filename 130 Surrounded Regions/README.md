# 130 Surrounded Regions

1 possible solution for this problem  

## Method 1

## Problem Intuition
We are given a grid of `X`s and `O`s, where `O` represents open regions. The task is to capture all surrounded regions by changing all `O`s that are completely surrounded by `X`s to `X`. However, any `O` connected to the border cannot be captured. We can optimize the solution by focusing on `O`s on the borders and marking all connected `O`s that should not be captured.

## Approach

### Key Idea
1. **Use DFS from Border Cells**: Start DFS from all `O`s on the borders, marking all connected `O`s as visited to indicate they should not be captured.
2. **Mark and Preserve Border-Connected Regions**: Replace any `O` connected to a border `O` with a temporary marker (`v`) to indicate it should be preserved.
3. **Final Transformation**: After marking, change all remaining `O`s (those not connected to the border) to `X`s, as they are surrounded. Change `v` back to `O` to restore the preserved regions.

### Step-by-Step Solution

1. **Loop Through Border Cells**:
   - **Rows**: For each cell in the first and last row, initiate DFS if the cell contains an `O`.
   - **Columns**: For each cell in the first and last column, initiate DFS if the cell contains an `O`.

2. **Define DFS Helper Function**:
   - **Input**: Current cell `(row, col)`.
   - **Base Cases**:
     - If the cell is out of bounds or does not contain an `O`, return.
   - **Process the Current Cell**:
     - Mark the cell with a temporary marker `v` to indicate it should be preserved.
   - **Recursive Calls**:
     - Perform DFS on all four adjacent cells (up, down, left, right) to continue marking connected `O`s.

3. **Final Transformation**:
   - After all DFS calls complete:
     - Loop through each cell in the grid.
       - Replace all `v`s with `O` to restore the preserved regions.
       - Replace all remaining `O`s with `X` as they are fully surrounded and not connected to the border.

4. **Return the Result**:
   - Since the grid is modified in-place, no need to return any value.

### Summary
- **DFS Logic**: By starting from border cells, we ensure only the `O`s that can reach the border remain unchanged.
- **Efficiency**: This approach avoids redundant checks and ensures only necessary cells are processed.
- **Output**: The grid is updated in-place with captured regions.


### Self Notes

```
"""
   we can solve this problem using dfs graph traversal 
      we can put a twist in the problem's approach
         instead of doing the operations from each O's
         we can do the operations from O's on the border
               replace any O's connected to a border O to 'v'
         in the end
               replace 'v's to O
               replace O's to X -- since they're not visited

   loop thru rows
      call recursive function for border cells
   loop thru cols
      call recursive function for border cells

   create helper function that implements recursively
      check for base conditions
         if location is out of bounds
         if location is not 0
      if above conditions are not true, it means this is connected to a border O
         we need to preserve this
      replace value to 'v'
      recursive call horizontal & vertical values
   
   in the end, loop thru grid
      replace 'v's to O
      replace O's to X -- since they're not visited
         they'd be visited if we need to have them in output
   
   since we're update values in-place, no need to return
"""
```
