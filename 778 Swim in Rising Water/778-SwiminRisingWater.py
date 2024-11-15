class Solution:
    """
    Djikstra's algorithm

    use Djikstra's algorithm to solve the problem
        the objective is to find the least amount of time until you reach the bottom right square (n-1,n-1)
        since it's an algo to find the shortest path, djistra's algorithm is the best

    create a set to record visited nodes -- so not to visit nodes again
    create a heap -- format: (time, row, col) -- time is the cumulative time taken to reach any particular spot
        populate heap with first value to kickstart the algo

    loop while minheap has values
        pop from heap
        check if the popped location is (n-1,n-1)
            we reached the destination, return time value of popped element
            since djikstra's algo is shortest path algo
                the first path to reach node (n-1,n-1) is the shortest path, hence we can return the value
            if this location is already in visited -- skip it
            now loop for horizontal & vertical directions
                check if the direction is out of bounds or in visited set
                    if not, add to heap
    
    since a solution is guaranteed, the return function will return a value
    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # visit set
        visited = set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # create heap
        minHeap = [(grid[0][0], 0, 0)] # format - (time, row, col)

        heapq.heapify(minHeap)

        # loop while minHeap has values
        while minHeap:
            # pop from heap to process
            tempTime, tempRow, tempCol = heapq.heappop(minHeap)

            if tempRow == n - 1 and tempCol == n - 1:
                return tempTime
            
            if (tempRow, tempCol) in visited:
                continue

            # add to visited
            visited.add((tempRow, tempCol))

            for dr, dc in directions:
                neiR, neiC = tempRow + dr, tempCol + dc

                # check if out of bounds & in visited
                if neiR < 0 or neiR == n or neiC < 0 or neiC == n or (neiR, neiC) in visited:
                    continue

                # add to heap
                heapq.heappush(minHeap, (max(tempTime, grid[neiR][neiC]), neiR, neiC)) 


    """
    My bruteforce dfs solution

    Time Limit Exceeded
    """
    # def swimInWater(self, grid: List[List[int]]) -> int:
    #     ROWS, COLS = len(grid), len(grid[0])

    #     visited = set()

    #     def dfs(r, c, maxRain):
    #         # base conditions
    #         # check out of bounds
    #         if r < 0 or r == ROWS or c < 0 or c == COLS:
    #             return 1000

    #         # check if in visited
    #         if (r, c) in visited:
    #             return 1000

    #         if r == ROWS - 1 and c == ROWS - 1:
    #             return max(maxRain, grid[r][c])

    #         # add to visited
    #         visited.add((r, c))

    #         # call all sides
    #         tempMinVal = min(dfs(r + 1, c, max(maxRain, grid[r][c])),
    #                     dfs(r - 1, c, max(maxRain, grid[r][c])),
    #                     dfs(r, c + 1, max(maxRain, grid[r][c])),
    #                     dfs(r, c - 1, max(maxRain, grid[r][c])))
            
    #         # cleanup visited
    #         visited.remove((r, c))

    #         return tempMinVal
        
    #     # for r in range(ROWS):
    #     #     for c in range(COLS):
    #     #         tempMaxRain = dfs(r, c, 0, grid[r][c])
    #     #         res = min(tempMaxRain, res)
        
    #     return dfs(0, 0, 0)