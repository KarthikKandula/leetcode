class Solution:
    """
    we can solve this problem using dfs graph traversal 
        we can put a twist in the problem's approach
            instead of doing the operations from empty rooms, we can do the operations from gates & work backwards
    
    create a queue & set to take note of visited values

    loop thru the entire input to find gates & insert into queue

    now loop while queue is not empty
        loop thru the queue in levels -- to increment distance value
            pop from queue
            update that location with distance 
            insert all the horizontal & vertical nodes that are empty rooms into queue
        increment distance value after each level
    
    since we're update values in-place, no need to return
    """
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # create variables for ROW & COL length
        ROWS, COLS = len(rooms), len(rooms[0])

        # create visited set
        visited = set()

        # create a queue for bfs ops
        queue = deque()

        # create helper function
        def addVal(r, c):
            # check if r, c are out of bounds
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return
            
            # check if r, c have already been visited or this location is an obstacle
            if (r, c) in visited or rooms[r][c] == -1:
                return
            
            # add to visited & queue
            visited.add((r, c))
            queue.append([r, c])

        # loop for rows
        for r in range(ROWS):
            # loop for cols
            for c in range(COLS):
                # check if location is a gate
                if rooms[r][c] == 0:
                    queue.append([r, c]) # add to queue
                    visited.add((r, c)) # add to visited
        
        # initialize variable for distance
        dist = 0
        
        # loop while queue has values
        while queue:
            # loop thru queue in levels
            maxLen = len(queue)
            # loop for current level
            for i in range(maxLen):
                # pop from queue 
                row, col = queue.popleft()

                # assign current distance value to location
                rooms[row][col] = dist

                # calls for horizontal & veritical rows
                addVal(row + 1, col)
                addVal(row - 1, col)
                addVal(row, col + 1)
                addVal(row, col - 1)

            # increment distance for next level
            dist += 1

