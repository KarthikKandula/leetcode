class Solution:
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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # define ROWS & COLS with length of rows & cols
        ROWS, COLS = len(board), len(board[0])

        # recursive function
        def dfs(r, c):
            # base condition checks
            # check if r, c is out of bounds
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return

            # check if r, c is not O
            if board[r][c] != 'O':
                return

            # change value to V -> visited
            board[r][c] = 'v'

            # recursive calls for horizontal & vertical positions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # loop thru ROWS to recursive call
        # Loop for no. of rows - Make dfs call for each border row
        for r in range(ROWS):
            # check if location is 0, to reduce function calls
            if board[r][0] == 'O':
                dfs(r, 0) # DFS call for border row positions
            # check if location is 0, to reduce function calls
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1) # DFS call for border row positions

        # loop thru COLS to recursive call
        # Loop for no. of cols - Make dfs call for each border col
        for c in range(COLS):
            # check if location is 0, to reduce function calls
            if board[0][c] == 'O':
                dfs(0, c) # DFS call for border col positions
            # check if location is 0, to reduce function calls
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c) # DFS call for border col positions

        # loop thru grid & replace values
        for r in range(ROWS): # loop thru rows
            for c in range(COLS): # loop thru cols
                # if position is visited -> need to keep it
                if board[r][c] == 'v':
                    board[r][c] = 'O'
                # if position is 0 --> can be captured aka replaced to X
                elif board[r][c] == 'O': 
                    board[r][c] = 'X'


