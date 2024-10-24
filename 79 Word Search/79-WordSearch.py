class Solution:
    """
    use backtracking to solve this problem
        acc to the problem description, we get certain understanding
        we have to visit all horizontally & vertically neighboring cells i.e., top, bottom, back, front
    
    take a set that keeps track of all locations visited for the current recursive trace
    call the recursive function for each position in the input

    create a hepler function that is implemented recursively
        input for this function is row, col positions & the current index in the word we're trying to search
        check if current word index is equal to the length of word 
            return true since we've found the word -- it wouldn't reach to this point if all other values didn't match
        check if current location is in bounds
            return false if not - row & col values has to be within input's bounds
        check if current location is equal to the current word's index
            return false if not
        add current location to path set
        make recursive calls for each direction i.e., top, bottom, back, front
        remove current location from path set -- to not affect other recursive stacks
        
        return true or false based on the return values from recursive calls
            it's an or condition, if one value is true we return true
        
    loop thru rows & cols of input & recursively call helper function for each location
        if returns true, return true -- word is found
    
    return False at end -- if true isn't returned above, word doesn't exist in input
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get ROW & COL length from input
        ROWS, COLS = len(board), len(board[0])
        path = set() # Use set() to track nodes already visited

        def backtracking(row, col, wrdIndex):
            # code here
            # check if word has been found
            if wrdIndex == len(word):
                return True

            # check if current location is out of bounds
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return False

            # check if current location is not equal to current location in word or if this location already visited
            if board[row][col] != word[wrdIndex] or (row, col) in path:
                return False

            # If program comes to this point, this is not visited & element exists in word
            # add current location to path
            path.add((row, col))

            # make recursive calls for horizontal & vertical cells
            res = (backtracking(row + 1, col, wrdIndex + 1) or 
                    backtracking(row - 1, col, wrdIndex + 1) or 
                    backtracking(row, col + 1, wrdIndex + 1) or
                    backtracking(row, col - 1, wrdIndex + 1))

            # cleanup path -- remove current position
            path.remove((row, col)) # removing since we've explored this location in current recursive path, but this location might be explored from other recursive paths, if it is not removed it'll affect those

            # return based on recursive call response
            return res

        # Loop through input rows
        for row in range(ROWS):
            # Loop through input cols
            for col in range(COLS):
                # Call Recursive function for each position in input board
                if backtracking(row, col, 0):
                    return True # If any position returns True, the problem is solved

        # If problem is not solved in above loop, it's not possible
        return False
