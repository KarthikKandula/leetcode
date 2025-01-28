class Solution:
    """
    This is a classic graph problem that uses bfs
        the twist in the problem is that need to use indexes as buses 
        since the index is the common point between buses
            also need to calculate the no. of hops required between indexes, helps to have a common value
        use sets to identify which buses & stops have been visited
        once visited a bus, add all the stops for that bus to q -- using input
            makes hopping between buses easier
            so, not only using a graph, also using the input array in the solution
        uses two data structures to efficiently get to the solution
    """
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # create graph
        graph = defaultdict(list)

        # populate graph in format stop: bus (index in routes)
        for i, route in enumerate(routes):
            # loop for each stop in current route
            for stop in route:
                # add current stop to graph
                graph[stop].append(i)

        # define variable to count no. of buses required
        level = 0

        # define queue to implement bfs
        q = deque()
        q.append(source) # add source to bfs to kickstart algo

        # take two sets to track stops & buses visited
        stops_visited = set()
        buses_visited = set()

        # initially add source to stops visited
        stops_visited.add(source)

        # loop while q is valid
        while q:
            # get length of current level aka stops
            stopsLen = len(q)

            # loop for all current stops
            for i in range(stopsLen):
                # processing all stops in the queue for this level
                stop = q.popleft()

                # if popped stop is the target
                if stop == target:
                    return level # return no. of levels, since reached target

                # take all buses for the current stop
                for bus in graph[stop]:
                    # check if this bus has been visited
                    if bus in buses_visited:
                        continue
                    
                    # this bus hasn't been visited
                    # add to visited set
                    buses_visited.add(bus)

                    # check each stop for this bus & see if it has been visited
                    # visit each stop under this bus & add to queue
                    for eachStop in routes[bus]:
                        if eachStop in stops_visited:
                            continue
                        
                        # if a stop for a bus hasn't been visited, add to set & queue
                        stops_visited.add(eachStop)
                        q.append(eachStop)

            # increment level after each bus is processed
            level += 1

        # return -1, since it's not possible to reach target if return not triggered inside
        return -1

