class Solution:
    """
    we treat this as a graph problem where each point is a node
        we use Prim's algorithm to solve this problem
        to solve using Prim's algorithm we need an adjacency list
        so we build an adjacency list where we calculate the distance between each node
        also, we name the nodes based on their indexes in input points.
    
    create a hashmap for adjacency list
        populate adjacency list by calcuating distance between two points -- do this between all points in list
        saved in format [cost, node]
    
    take a result variable -- initialized to 0
    take a visited set
    take a minHeap
        initialize it to [0, 0] to kickoff the algorithm
        this means we're visiting node 0 in the first iteration which will add all node 0's neighbors to the minheap
    
    implementing prim's algorithm
        loop while visited length is less than num of points -- aka not all nodes have been visited
        pop from minHeap -- get's the node with smallest distance
        check if it's already in visited
            if yes, skip iteration
        if not, this is a new node & we need to make the connection
        add to visited
        add cost to result variable
        loop thru this node's neighbors
            add all nodes to minHeap if they're not in visited
    
    once all nodes have been visisted, result is in the variable, return it
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # get no. of points
        numPoints = len(points)

        # create empty adjList 
        adjMap = {i:[] for i in range(numPoints)}

        # populate adjacency list with the dist & node
        for i in range(numPoints):
            # get first point from points
            x1, y1 = points[i]
            # loop thru every other point -- other than one from above
            # calculating distance between each & every point
            for j in range(i + 1, numPoints):
                # get second point from points
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2) # get distance between two points

                # append to i & j since undirected
                adjMap[i].append([dist, j])
                adjMap[j].append([dist, i])
        
        # until now we've done the grunt work for creating an adjList to before implementing Prim's algo

        # result variable
        res = 0
        visited = set() # visited set to not visit a node twice
        minHeap = [[0, 0]] # initialize with neutral position

        # heapify heap
        heapq.heapify(minHeap)

        # loop while visited is less than the num of points -- once it has all points, we stop the loop
        while len(visited) < numPoints:
            # pop from heap - this is the node that is in consideration to be connected
            cost, node = heapq.heappop(minHeap)
            # skip any ops if node is already in visited
            if node in visited:
                continue
            
            # reaches here if node has not been visited
            visited.add(node)
            res += cost # add current node's cost to result

            # loop thru each neighbor for this node & add to heap
            for eachCost, eachNei in adjMap[node]:
                # only if it isn't already in node
                if eachNei not in visited:
                    # push to heap
                    heapq.heappush(minHeap, [eachCost, eachNei])
        
        # return result
        return res

