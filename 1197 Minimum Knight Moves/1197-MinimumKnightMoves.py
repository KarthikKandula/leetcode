class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # absolute x & y values to make it symmetrical, by reducing quadrants this value can scale up
        x, y = abs(x), abs(y)

        # create queue to implement bfs
        q = deque()
        # append starting node to queue
        q.append([0, 0, 0])
        
        # create set to keep track of visited locations
        visited = set()

        # create array for all possible moves from a position
        allMoves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, 2], [-2, 1]] # , [-2, -1], [-1, -2]
        # allMoves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]

        # loop while q is initialized
        while q:
            # pop from queue
            r, c, m = q.popleft()

            # check if popped value is target
            if r == x and c == y:
                return m # if yes, return moves 

            # loop thru all possible moves at this location
            for mr, mc in allMoves:
                # get updated r, c values
                nr, nc = r + mr, c + mc

                # if this new r, c value is in visited, skip
                if (nr, nc) not in visited:
                    # if not
                    # add to visited set
                    visited.add((nr, nc))
                    # add to queue, add 1 move
                    q.append([nr, nc, m + 1])

        # no need to return anything since answer is guaranteed
