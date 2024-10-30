class Solution:
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create sets for cols, posDiag, negDiag
        cols = set()
        posDiag = set()
        negDiag = set()

        # result array
        res = []
        # create default board
        board = [['.'] * n for i in range(n)]

        # create helper function
        def backtracking(r):
            # base condition
            if r == n: # means this is out of bounds
                # copy current board to result
                copyBoard = ["".join(eachRow) for eachRow in board] 
                res.append(copyBoard)
                return
            
            # actual functionality
            for c in range(n):
                # check if current pos exists in cols, posDiag, negDiag
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue 
                
                # if doesn't exists in any of the above
                # add current pos to cols, posDiag, negDiag
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                # recursive call
                backtracking(r + 1)

                # cleanup sets & board for future ops
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

        
        # initial function call
        backtracking(0) # passing row values

        # return result array
        return res

