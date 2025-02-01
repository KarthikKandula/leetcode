class Solution:
    """
    this is an extension of the largest island problem
        to solve the problem
        we need to first know all the islands
        then find out by flipping which 0 value, we can form the biggest island

        get all islands & their r, c values in a hashmap
            assign a unique identifier to each island
        record the size of each island via it's unique identifier

        go thru each 0 & check it's 4-directional values
            sum sizes of everything & check if it's the max
        
        in the end, return the max value
    """
    def largestIsland(self, grid: List[List[int]]) -> int:
        # get rows & cols in a variable
        ROWS, COLS = len(grid), len(grid[0])

        # recursive function
        def dfs(r, c, islandID):
            # base conditions
            # if r, c out of bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0

            # if r, c visited
            if (r, c) in visited:
                return 0

            # if r, c doesn't count
            if grid[r][c] == 0:
                return 0

            # if reaches here, this cell is a 1 & needs to be visited
            visited.add((r, c))
            islandIDs[(r, c)] = islandID # add this r, c to the island's hashmap 

            # call 4 directions
            bottom = dfs(r + 1, c, islandID)
            top = dfs(r - 1, c, islandID)
            right = dfs(r, c + 1, islandID)
            left = dfs(r, c - 1, islandID)

            # return total area for this cell
            return 1 + top + bottom + left + right
        
        visited = set() # to track all visited nodes
        islandIDs = {} # to store (r, c) with their id's
        islandSizes = {} # to store id's: island sizes
        maxIsland = 0 # to record max island value
        islandID = 1 # to track island id's 

        # loop for each (r, c)
        for r in range(ROWS):
            for c in range(COLS):
                # if this val is a 1 & hasn't been visited before
                if grid[r][c] == 1 and (r, c) not in visited:
                    # call recursive function
                    island = dfs(r, c, islandID)
                    maxIsland = max(maxIsland, island) # update max island value

                    # assign the island size for this island id
                    islandSizes[islandID] = island

                    islandID += 1 # increment island value for next island

        # array to indicate directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0 # to store result value

        # loop fore each r, c
        for r in range(ROWS):
            for c in range(COLS):
                # if this value is 0, can be flipped
                if grid[r][c] == 0:
                    temp = 0 # value to calculate area if this 0 is flipped
                    islandSet = set() # set to track all island id's this cell neighbors

                    # loop for each value in directions
                    for dr, dc in directions:
                        # calc new cell value
                        nr, nc = r + dr, c + dc

                        # if new cell is a 1 i.e, exists in islands hashmap 
                        if (nr, nc) in islandIDs:
                            islandSet.add(islandIDs[(nr, nc)]) # add the island id to set

                    # for each island id in the set, add it's size to temp value
                    for eachId in islandSet:
                        temp += islandSizes.get(eachId, 0)
                    
                    # get max area of updated islands
                    res = max(res, temp + 1)

        # return largest island value based on condition
        return maxIsland if res == 0 else res
