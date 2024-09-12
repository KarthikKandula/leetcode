class Solution:
    """
    Use hashset to solve the problem
        Since sets are always unique, it's a good idea to use them in a hashmap
    
    Have a hashset for rows, cols & 3x3 boxes
        the key structure for 3x3 boxes hashset is a bit different since 
        we're considering all the values in a single 3x3 box as one hashset

        We're using a tuple (r//3, c//3) as a key in 3x3 boxes hashset

    Loop thru each value in nested loops
        check if the current value is already in any of the hashsets, if exists return false
        if not, insert the value in all 3 hashsets
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Create a hashmap with set for rows aka hashset
        cols = defaultdict(set) # Create a hashmap with set for columns aka hashset
        boxes = defaultdict(set) # Create a hashmap with set for 3x3 boxes aka hashset
        # key for boxes hashset is a tuple - (r//3, c//3)

        # loop thru rows
        for r in range(9):
            # loop thru columns
            for c in range(9):
                # Check if current position is empty 
                if board[r][c] == '.':
                    continue
                # Check if current position value is already in rows set for this index 
                if board[r][c] in rows[r]:
                    return False
                # Check if current position value is already in cols set for this index 
                if board[r][c] in cols[c]:
                    return False
                # Check if current position value is already in boxes set for this index (using boxes' key)
                if board[r][c] in boxes[(r//3, c//3)]:
                    return False

                rows[r].add(board[r][c]) # add current value to corresponding rows hashset
                cols[c].add(board[r][c]) # add current value to corresponding cols hashset
                boxes[(r//3, c//3)].add(board[r][c]) # add current value to corresponding boxes hashset
        
        # If loop reaches this position, it's a valid sudoku
        return True
