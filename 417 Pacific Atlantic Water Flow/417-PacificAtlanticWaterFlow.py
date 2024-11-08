class Solution:
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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set() # will operate as visited & record all locations possible to reach this ocean
        atlantic = set() # will operate as visited & record all locations possible to reach this ocean

        def checkOcean(r, c, visited, prevValue):
            # check if r, c out of bounds
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return

            # check if r, c in visited
            if (r, c) in visited:
                return

            # check if prev value > r, c
            if prevValue > heights[r][c]:
                return
            
            # If all above conditions are not satisfied, this position is reachable to either ocean
            # Add position/node to visited set - auto adds to respective set
            # add r, c to visited
            visited.add((r, c))

            # recursive calls for horizontal & vertical cells
            checkOcean(r + 1, c, visited, heights[r][c])
            checkOcean(r - 1, c, visited, heights[r][c])
            checkOcean(r, c + 1, visited, heights[r][c])
            checkOcean(r, c - 1, visited, heights[r][c])

        # loop thru ROWS to recursive call
        # Loop for no. of rows - Make dfs call for each border row for both oceans
        for r in range(ROWS):
            checkOcean(r, 0, pacific, heights[r][0]) # DFS call for border row positions for pacific ocean
            checkOcean(r, COLS - 1, atlantic, heights[r][COLS - 1]) # DFS call for border positions for atlantic ocean
        
        # loop thru COLS to recursive call
        # Loop for no. of cols - Make dfs call for each border col for both oceans
        for c in range(COLS):
            checkOcean(0, c, pacific, heights[0][c]) # DFS call for border col positions for pacific ocean
            checkOcean(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # DFS call for border positions for atlantic ocean

        # output result variable
        res = []

        # Loop through input rows & cols 
        for r in range(ROWS):
            for c in range(COLS):
                # Check if this position is in both atlantic & pacific sets
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c]) # If yes, add to result array

        return res
