class Solution:
    """
    using Bellman-Ford Algo

    this is a graph-traversal problem which will be better to use Bellman-Ford
        Bellman-Ford is best to find the shortest path to every node
        this will be achieved by only looping thru the input/graph k + 1 times -- derived from problem desc
        if the value isn't set in k + 1 loops, it means no path exists, so we return -1

    create an array with inf values for each node
        replace source node's to 0 -- since starting there
    
    loop thru the input k + 1 times
        before each loop, create a temp array -- copy of above array
            so it doesn't interfere with the value updates done in current loop
        while looking at each node, if any node's value in inf
            it means it hasn't yet been looked at, skip that value
        if at any point the node's source value + price < destination value from temparray
            replace value in temparray
        assign temparray values to actual array
    
    in the end after loop is done, return values based on problem condition
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create an array with inf values for each node to record shortest path
        paths = [float('inf') for i in range(n)]

        # update src path value
        paths[src] = 0

        # start loop -- will loop a max of k + 1 times
        for i in range(k + 1):
            # create a copy of paths -- to perform ops for this loop
            tempPaths = paths.copy()

            # loop thru input flights
            for source, dest, thisK in flights:
                # if paths value is infinity -- this node hasn't been visited yet, can ignore
                if paths[source] == float('inf'):
                    continue
                
                # check if cost from this source & this cost is less than dest's value in tempPaths
                if paths[source] + thisK < tempPaths[dest]:
                    tempPaths[dest] = paths[source] + thisK # if yes, replace the value -- we found a new lowest value
            
            # replace paths with tempPaths
            paths = tempPaths

        # return paths value based on condition in prblm statement
        return paths[dst] if paths[dst] != float('inf') else -1


    """
    using Djikstra's algo

    work in progress
    """
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #     adjList = {i: [] for i in range(n)}

    #     for frm, to, price in flights:
    #         adjList[frm].append([to, price])
        
    #     minHeap = [(src, 0, -1)] # format - toNode, cost, curr k
    #     visited = set()
    #     res = float("inf")

    #     while minHeap:
    #         # pop from heap
    #         to, cost, currK = heapq.heappop(minHeap):

    #         # check if result is good
    #         if currK <= k and to == k:
    #             res = max(cost, res)
            
    #         # go thru each neighbor
    #         for eachNei, eachCost in 