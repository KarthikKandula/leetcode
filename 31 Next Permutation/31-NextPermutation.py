class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # get length of rows & cols
        ROWS, COLS = len(grid), len(grid[0])

        # create queue to implement bfs
        q = deque()

        # loop thru each location & get all food locations
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '#':
                    q.append((r, c)) # append (r, c) to queue if it is food

        level = 1 # variable to track current level

        # define directions for easier implementation
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # loop thru queue
        while q:
            # get length of the current queue level
            qLen = len(q)

            # loop thru current queue level
            for i in range(qLen):
                # pop from queue
                qr, qc = q.popleft()

                # loop for each direction
                for dr, dc in directions:
                    # get new r, c locations
                    nr, nc = qr + dr, qc + dc

                    # if out of bounds
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    
                    # if value is obstacle or food cell --> continue
                    if grid[nr][nc] == 'X' or grid[nr][nc] == '#':
                        continue
                    
                    # if new location is food, return level value
                    if grid[nr][nc] == '*':
                        return level
                    
                    # if not, it's an empty space
                    # update value to X to avoid revisit
                    grid[nr][nc] = 'X'

                    # append new location to queue
                    q.append((nr, nc))
            
            # increment level to indicate another level has completed
            level += 1

        # return -1 if return is not hit inside
        return -1
