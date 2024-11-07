class Solution:
    """
    we can solve this problem using bfs graph traversal
        we can put a twist in the problem's approach
        instead of doing the operations from fresh oranges
        we can do the operations from rotten oranges & work backwards

    create a queue keep track of rotten oranges 
        insert all rotten oranges into queue in one loop thru entire grid
    variable to track fresh oranges
        count no of fresh oranges in one loop thru entire grid

    loop while queue is not empty & fresh count is greater than 0
        loop thru queue in levels -- to increment time value
            pop from queue
            insert all horizontal & vertical spots that are fresh oranges into queue
                update value to rotten
                decrement frsh count
        increment time after each level
    
    since we're returning the time, by the end of loop, time would be in variable
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get ROW & COL length -- store in variables
        ROWS, COLS = len(grid), len(grid[0])

        # queue to keep track of bfs
        queue = deque()

        # variables to keep track of time & fresh oranges
        time, fresh = 0, 0

        # Loop through input grid to populate fresh & queue
        for r in range(ROWS):
            for c in range(COLS):
                # # If this position == 1, increment fresh 
                if grid[r][c] == 1:
                    fresh += 1 # By the end, we'll have the count of fresh oranges
                # If this position == 2, add to queue
                elif grid[r][c] == 2:
                    queue.append((r, c)) # By the end, we'll have all rotten oranges in queue ready to be processed
        
        # Loop while queue is not emptty & fresh > 0 - to end early if fresh = 0
        while queue and fresh > 0:
            # Get length of queue at this point - helps with bfs since looping only for current level
            qLen = len(queue)

            # Loop for qLen
            for i in range(qLen):
                # pop from queue
                row, col = queue.popleft()

                # All possible directions, horizontal & vertical
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

                # Loop for each possible direction
                for dr, dc in directions:
                    # Add popped row & col to directions row & col -- row, col we'll be checking
                    tr = row + dr
                    tc = col + dc

                    # Check if tr & tc are in range & this position/node is a fresh orange
                    if tr >= 0 and tr < ROWS and tc >= 0 and tc < COLS and grid[tr][tc] == 1:
                        grid[tr][tc] = 2 # If yes, replace with rotten orange
                        queue.append((tr, tc)) # Add this rotten orange to queue for processing

                        fresh -= 1 # Decrement fresh by 1, since a fresh orange has rotten

            # After a level of bfs processing, incrment time by 1
            time += 1
        
        # return time if fresh = 0 i.e all fresh oranges have been replaced else -1
        return time if fresh == 0 else -1



