class Solution:
    """
    Recursive solution

    we can solve this using Recursive DFS algorithm
        the entire logic of this problem is
        find the no of islands by knowing which locations have already been visited
            once a location with 1 is found, increment count
            add all adjacent 1's to visited -- count will not be increased for these
                if in future these are visited, we'll not increment count since they're in visited
            in essence increment count for the first 1 we hit & the rest will not be hit since they'll be visited by 1st 1
    
    loop thru each grid location in a nested loop
        to reduce no. of function calls
        check if location is 1 & if this isn't visited
            increment 

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

    after code runs for all locations, we'll have the count in output variable
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # get length of row & col values
        ROWS, COLS = len(grid), len(grid[0])

        # create set for recording visited nodes
        visited = set()
        output = 0 # output variable

        # helper function to implement bfs
        def bfs(r, c):
            # check if r, c are out of bounds
            if r not in range(ROWS) or c not in range(COLS):
                return

            # check if r, c already visited
            if (r, c) in visited:
                return

            # check if position is 0
            if grid[r][c] != '1':
                return

            # add to visited
            visited.add((r, c))

            # recursive calls for horizontal & vertical cells
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

        # loop for length of rows
        for r in range(ROWS):
            # loop for length of cols
            for c in range(COLS):
                # check if current position is an island & it's not been visited
                if grid[r][c] == '1' and (r, c) not in visited: 
                    bfs(r, c) # function call for this location
                    output += 1 # increment output, found an island
        
        return output

    """
    Iterative bfs solution

    we can solve this using Iterative BFS algorithm
        the entire logic of this problem is
        find the no of islands by knowing which locations have already been visited
            once a location with 1 is found, increment count
            add all adjacent 1's to visited -- count will not be increased for these
                if in future these are visited, we'll not increment count since they're in visited
            in essence increment count for the first 1 we hit & the rest will not be hit since they'll be visited by 1st 1
    
    after code runs for all locations, we'll have the count in output variable
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # get length of row & col values
        ROWS, COLS = len(grid), len(grid[0])
        
        # create set for recording visited nodes
        visited = set()
        output = 0 # output variable

        # helper function to implement bfs
        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            # loop while queue has values
            while queue:
                # pop from queue
                row, col = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dr, dc in directions:
                    # update row & col to new directions
                    r = row + dr
                    c = col + dc

                    # check if r, c are out of bounds
                    # check if r, c already visited
                    # check if position is 0
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == '1':
                        # it's an island, we need to visit 
                        visited.add((r, c))
                        queue.append((r, c))

        # loop for length of rows
        for r in range(ROWS):
            # loop for length of cols
            for c in range(COLS):
                # check if current position is an island & it's not been visited
                if grid[r][c] == '1' and (r, c) not in visited: 
                    bfs(r, c) # function call for this location
                    output += 1 # increment output, found an island
        
        return output
