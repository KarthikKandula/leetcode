class Solution:
    """
    Iterative Solution
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # get starting color into a variabe
        startcolor = image[sr][sc]
        
        # if start color is same as final color, no need to make any changes
        if startcolor == color:
            return image 

        # create queue to implement bfs
        q = deque()
        q.append((sr, sc)) # append starting location to kickstart algo

        # get rows & cols into a variable
        ROWS, COLS = len(image), len(image[0])

        # create visited set, to avoid cycles
        visited = set()
        # create possible directions for easy access
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # loop while queue has values
        while q:
            # get queue length
            qLen = len(q)

            # loop for current loop length
            for i in range(qLen):
                # pop from queue
                r, c = q.popleft()

                # update color in current location
                image[r][c] = color

                # loop for all directions
                for dr, dc in directions:
                    # update to next direction
                    nr, nc = dr + r, dc + c

                    # if r, c out of bounds
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    
                    # if r, c already visited or not same as start color
                    if (nr, nc) in visited or image[nr][nc] != startcolor:
                        continue
                    
                    # add to visited
                    visited.add((nr, nc))

                    # append to queue
                    q.append((nr, nc))

        # return modified/updated image
        return image

    """
    Recursive Solution
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # get starting color into a variabe
        startcolor = image[sr][sc]
        
        # if start color is same as final color, no need to make any changes
        if startcolor == color:
            return image 
        
        # get rows & cols into a variable
        ROWS, COLS = len(image), len(image[0])

        # create visited set, to avoid cycles
        visited = set()

        # recursive function to implement dfs
        def dfs(r, c):
            # base conditions
            # if r, c out of bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            
            # if r, c already visited or not same as start color
            if (r, c) in visited or image[r][c] != startcolor:
                return
            
            # add to visited
            visited.add((r, c))

            # update color on current location
            image[r][c] = color

            # calls to 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # initial call from start location
        dfs(sr, sc)

        # return updated matrix
        return image
