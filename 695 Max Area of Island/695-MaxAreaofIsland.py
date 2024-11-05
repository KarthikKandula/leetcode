class Solution:
    """
    Recursive DFS solution

    we can solve this using Recursive DFS algorithm
    
    loop thru each grid location in a nested loop
        to reduce no. of function calls
        check if location is 1 & if this isn't visited
        once a function returns, update max value to output

    create a helper recursive dfs function
        input is row & columns
        check if this row & col are out of bounds
            return
        check if this location is already visited
            return
        check if this location isn't an island
            return
        if reaches this point, means it's not visited & an island
        add to visited 
        make recursive calls for horizontal & vertical cells

        in the end return sum of all recursive calls along with 1 -- to account for current location

    after code runs for all locations, we'll have the count in output variable
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get length of row & col values
        ROWS, COLS = len(grid), len(grid[0])

        # create set for recording visited nodes
        visited = set()
        output = 0 # output variable

        # helper function to implement bfs
        def bfs(r, c):
            # check if r, c are out of bounds
            if r not in range(ROWS) or c not in range(COLS):
                return 0

            # check if r, c already visited
            if (r, c) in visited:
                return 0

            # check if position is 0
            if grid[r][c] == 0:
                return 0

            # add to visited
            visited.add((r, c))

            # recursive calls for horizontal & vertical cells
            # ar = bfs(r + 1, c, count)
            # br = bfs(r - 1, c, count)
            # cr = bfs(r, c + 1, count)
            # dr = bfs(r, c - 1, count)

            # return 1 + ar + br + cr + dr

            # recursive calls for horizontal & vertical cells
            return 1 + bfs(r + 1, c) + bfs(r - 1, c) + bfs(r, c + 1) + bfs(r, c - 1)

        # loop for length of rows
        for r in range(ROWS):
            # loop for length of cols
            for c in range(COLS):
                # check if current position is an island & it's not been visited
                if grid[r][c] == 1 and (r, c) not in visited: 
                    tempOutput = bfs(r, c) # function call for this location
                    output = max(tempOutput, output) # get max output value
        
        return output

    """
    Iterative BFS solution
        we can solve this using Iterative BFS algorithm
        the entire logic of this problem is
        find the max area of islands by knowing which locations have already been visited
        know the area of each island by creating a local variable & increment it everytime 1 is found adjacent
        replace output value with max of each area of an island
    
    after code runs for all locations, we'll have the count in output variable
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get length of row & col values
        ROWS, COLS = len(grid), len(grid[0])

        # create set for recording visited nodes
        visited = set()
        output = 0 # output variable
    
        # helper function to implement bfs
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            res = 1 # initialized to 1 to account for current location

            # loop while queue has values
            while queue:
                # pop from queue
                row, col = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dr, dc in directions:
                    # update row & col to new directions
                    tr = row + dr
                    tc = col + dc

                    # check if r & c are out of bounds
                    # chec if r & c are in visited
                    # check if location is 1
                    if tr in range(ROWS) and tc in range(COLS) and (tr, tc) not in visited and grid[tr][tc] == 1:
                        # it's an island, we need to visit 
                        queue.append((tr, tc))
                        visited.add((tr, tc))
                        res += 1 # increment result
            
            # return res - length of current island
            return res

        # loop for length of rows
        for r in range(ROWS):
            # loop for length of cols
            for c in range(COLS):
                # check if current position is an island & it's not been visited
                if grid[r][c] == 1 and (r, c) not in visited: 
                    tempOutput = bfs(r, c) # function call for this location
                    output = max(tempOutput, output) # get max output value
        
        return output