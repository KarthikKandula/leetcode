class Solution:
    """
    optimal solution

    the way minimum height trees work is that there can only be 1 or 2 MHT's
        cuz if there is a tree with 3 nodes of equal height values, the middle node is the MHT
        using this logic, we can come to the conclusion that if we start removing leaf nodes
            iteratively remove leaf nodes
            in the end, there will only be 1 or 2 nodes left & those nodes will be the MHT
            keep eliminating leaf nodes
                in the process if any new leaf nodes are created, eliminate them as well
                only 1 or 2 nodes will be remaining, those are the MHT's

        build an adjacency list
        build an array with no of connections in a diff array -- heights
        get all nodes with only 1 connection in the queue
        process each node & reduce the count of neighbors from heights array
            if any neighbor's height becomes 1, add it to the queue
            if the remaining node's become 1 or 2, those are the MHT's, return a list with these nodes
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # if number of edges is less than 2, they are the MHT's
        if n <= 2:
            return [i for i in range(n)]
        
        # create adjList
        neighbors = {i:[] for i in range(n)}
        
        # create array to record no. of connections for each node
        heights = [0] * n

        # populate adjList
        for a, b in edges:
            # since undirected, add values to either nodes
            neighbors[a].append(b)
            neighbors[b].append(a)

            # increment height for each node
            heights[a] += 1
            heights[b] += 1

        # create queue
        q = deque()

        # add nodes with height 1 to queue
        for i, v in enumerate(heights):
            if v == 1:
                q.append(i)

        # variable to track remaining nodes
        remaining = n

        # loop until remaining nodes are 2 or less
        while remaining > 2:
            # get length of queue
            qLen = len(q)

            # subtract these nodes from the remaining number
            remaining -= qLen

            # process all the nodes in a loop
            for i in range(qLen):
                # pop a node from queue
                leaf = q.popleft()

                # decrement height for this leaf, since it's popped
                heights[leaf] -= 1

                # loop for each neighbor for the leaf node
                for nei in neighbors[leaf]:
                    # decrement height for this neighbor since this node is being eliminated
                    heights[nei] -= 1

                    # if any node's height is down to 1, add to queue to processing
                    if heights[nei] == 1:
                        q.append(nei)

        # by end of loop, MHT's are in queue
        return list(q)

    """
    TLE solution
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adjList
        adjlist = {i:[] for i in range(n)}

        # populate adjList
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)

        visit = set()

        # recursive function
        def dfs(node):
            visit.add(node)

            height = 0

            for nei in adjlist[node]:
                if nei not in visit:
                    height = max(height, dfs(nei))

            visit.remove(node)

            return height + 1

        cache = {}
        minHeight = n

        # loop for each node
        for i in range(n):
            temp = dfs(i) - 1
            cache[i] = temp
            minHeight = min(minHeight, temp)

        # get min value from cache
        res = []

        for key, val in cache.items():
            if val == minHeight:
                res.append(key)

        return res
