class Solution:
    """
    we can solve this problem using dfs matrix traversal
        since the request is to modify board in-place
            we come up with a notation that indicates orig & target values
            design our calculations around the made up notation
        in this case the notation is as follows
            orig    new    translation
            0       0       0
            1       0       1
            0       1       2
            1       1       3
        
        after reading the prob desc we come to conclusion that
            if orig value is 1 & count is 2 or 3
                update value to 3
            if orig value is 0 & count == 3
                update value to 2
        
        we need to take the above values into consideration while calcuating the count of adjacent nodes
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # get row & cols values into a constant
        ROWS, COLS = len(board), len(board[0])

        # helper function to get count of any index
        def getCount(r, c):
            count = 0 # intitialize temp count value
            # loop thru every location & get count
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    # skip out of bounds values
                    if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                        continue
                    # skip curr location
                    if i == r and j == c:
                        continue

                    # if val is 1, increment count
                    if board[i][j] in [1, 3]:
                        count += 1

            return count # return count val

        # traverse every location & call helper function
        for r in range(ROWS):
            for c in range(COLS):
                count = getCount(r, c)

                # if curr val is 1
                if board[r][c] == 1:
                    # if count is either 2 or 3
                    if count in [2, 3]:
                        board[r][c] = 3 # update value to 3, indicating it's going to be 1
                # if orig value is 0
                else:
                    # if count is 3
                    if count == 3:
                        board[r][c] = 2 # update value to 2, since it's going to be alive
        
        # pass thru each location & update values
        for r in range(ROWS):
            for c in range(COLS):
                # if updated value is 1, change to 0
                if board[r][c] == 1:
                    board[r][c] = 0
                # if updated value is 2 or 3, change to 1
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

