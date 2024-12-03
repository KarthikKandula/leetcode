class Solution:
    """
    NeetCode constant space solution

    to solve this problem in constant space
        we can use the first row & col as indicators for their respective row & cols
        until we run into a problem since [0][0] is common for both row & col
            we'll use a different variable to indicate for the first row
    
    loop thru matrix to mark first row/col to 0
        only other than for the first row, since we created a seperate variable for that
    
    loop thru matrix to update values 
        only looping from 1 -> end for row & cols
        handling 0th row & index seperate
    
    check if [0][0] value is 0
        this is the indicator for first column, if it is, update values
    
    check if 0th row flag is True
        this is the indicator for first row, if it is, update rows
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # get row & col length
        ROWS, COLS = len(matrix), len(matrix[0])

        # boolean variable to track if top row needs to be Zero
        rowZero = False

        # loop thru matrix to mark first row, col 0
        for r in range(ROWS):
            for c in range(COLS):
                # if this location is 0
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # update top value in this column to be 0

                    # before updating the row indicator, check if row is greater than 0
                    if r > 0:
                        matrix[r][0] = 0 # update value if row is greater than 0
                    else:
                        rowZero = True # else, update the value
        
        # loop thru matrix to update values to 0
        for r in range(1, ROWS): # loop from 1 -> end -- handling 0th row later
            for c in range(1, COLS): # loop from 1 -> end -- handling 0th col later
                # if either 0th index row or column value is 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0 # update the value to 0
        
        # update first column, check if [0][0] is 0, this indicates first column has to be 0
        if matrix[0][0] == 0:
            for r in range(ROWS): # loop thru rows
                matrix[r][0] = 0 # update each value with column as 0

        # update first row, check if flag is True, this indicates first row has to be 0
        if rowZero:
            for c in range(COLS): # loop thru cols
                matrix[0][c] = 0 # update each value with row as 0

    """
    My O(m + n) solution

    The idea is to use two sets
        one for rows & one for cols to record which rows/cols need to be made 0's
        using sets since there will not be any duplicates
    
    loop thru matrix once to populate sets
    loop thru matrix again to update values based on values in sets
    """
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     # create sets for rows & cols
    #     rows, cols = set(), set()

    #     # loop thru rows & cols to populate sets
    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             if matrix[r][c] == 0:
    #                 rows.add(r) # add row value to set
    #                 cols.add(c) # add col value to set

    #     # loop thru rows & cols again to update values based on values in set
    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             if r in rows or c in cols: # if this row/col is in either sets
    #                 matrix[r][c] = 0 # update that value to 0

