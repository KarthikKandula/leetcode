# 51. N-Queens

1 possible solution for this problem  

## Method 1

## Problem Intuition
The N-Queens problem asks you to place N queens on an N×N chessboard such that no two queens can attack each other. In chess, queens can move horizontally, vertically, and diagonally. This leads to the following key observations:

1. **One Queen per Row and Column**: We can only have one queen in each row and column.
2. **Tracking Attack Paths**: We need to keep track of columns, positive diagonals (`row + col`), and negative diagonals (`row - col`) to identify safe positions for placing queens.

## Approach
### Step 1: Initialize Data Structures
- **Empty Board**: Create an N×N board initialized with dots (`.`) representing empty cells.
- **Tracking Sets**: Create sets to keep track of occupied columns (`cols`), positive diagonals (`posDiag`), and negative diagonals (`negDiag`).

### Step 2: Create a Helper Function for Recursive Backtracking
The helper function will recursively attempt to place queens in each row.

- **Input**: The current row number.

### Step 3: Define the Base Case
- If the current row number equals `N`:
  - A valid configuration has been found, so convert the current board state into a list of strings and append it to the result array.
  - Return to stop further recursion along this path.

### Step 4: Iterate Over All Columns in the Current Row
- For each column in the current row:
  - Check if the `(row, col)` combination is already under attack (i.e., if it exists in any of the sets `cols`, `posDiag`, or `negDiag`).
  - If it is, continue to the next column.

### Step 5: Place the Queen and Update Sets
- Add the current column, positive diagonal (`row + col`), and negative diagonal (`row - col`) to their respective sets.
- Place a queen (`'Q'`) on the board at the current `(row, col)` position.

### Step 6: Recursively Call the Helper Function for the Next Row
- Move to the next row and continue the placement of queens using recursive calls.

### Step 7: Backtrack (Cleanup)
- Remove the queen from the board (`'.'`) and remove the current column, positive diagonal, and negative diagonal from their respective sets. This ensures that the next placement attempt does not conflict with the current configuration.

### Step 8: Return the Result Array
- Once all recursive calls are complete, the result array will contain all valid solutions.
- Return the result array as the final solution.

### Self Notes


```
"""
   use backtracking to solve the problem
      by the way chess works, queens can go horizontal, vertical & diagonal
         so by this we know, we can only have one queen in any row or col
         if we keep track of which cols, positive diagonal, negative diagonal a queen is in
         perform backtracking ops mainly for each row, solution is going to be easy

   initialize an empty board with .'s
   create sets for keeping track of cols, posDiag & negDiag

   create a helper function to implement recursive backtracking
      input to this function is row number
      check if row number is equal to input n -- base condition
         append current board to result array -- found a solution
         return from function
      loop thru all the cols in current row
         check if current (row, col) combination exists in either cols, posDiag or negDiag
               if it does, continue
         add current position to all three sets
         change current position to a 'Q' in board
         recursively call for next row

         cleanup all three sets & current position to a '.' in board
               for future operations
   
   once all functions return, result is in result array, return it
"""
```
