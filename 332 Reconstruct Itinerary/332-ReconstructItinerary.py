class Solution:
    """
    we can treat this as a graph traversal problem where each airport is a node
        each ticket represents a directed edge, forming a path between airports
        the goal is to find a valid Eulerian path starting from "JFK" 
        in lexicographical order to form the itinerary
    
    create a hashmap to represent the graph (adjacency list)
        use a sorted order to add destinations for each airport
        add destinations in reverse sorted order to allow efficient traversal using pop() 
    
    create an empty list to store the final itinerary
        initialize a helper function for depth-first search (DFS) traversal
        this DFS uses post-order insertion to build the itinerary

    create a helper function to perform DFS
        input is an airport (node) in the graph
        loop while the airport has destinations, removing each destination and calling DFS recursively
        after all reachable destinations from this airport are processed, add this airport to the itinerary

    begin DFS from "JFK" as the required starting point
        each airport is added to the itinerary only after all destinations are exhausted
        reversing the final itinerary gives the correct order
    
    by the end of DFS, the itinerary list contains the desired path in the correct order
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create hashmap for creating adjacency list
        graph = defaultdict(list)

        # populate src & destination to adjacency list in reverse sorted order
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        # create empty array to hold itinerary
        itinerary = []

        # helper function to implement recrusive dfs
        def dfs(airport):
            # loop while this airport has destinations in hashmap
            while graph[airport]:
                # recursively call function with popped value -- calling from right to left, hence reverse sorted order
                dfs(graph[airport].pop())
            
            # add this airport to itinerary
            itinerary.append(airport)

        # initial function call
        dfs("JFK")

        # return itinerary in reversed order since inserting in reverse order
        return itinerary[::-1]

    """
    This solution is called Hierholzer's Algorithm

    learn later
    """
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     graph = collections.defaultdict(list)
    #     for src, des in tickets:
    #         graph[src].append(des)
        
    #     for src in graph:
    #         graph[src].sort(reverse = True)
        
    #     stack = ['JFK']
    #     res = []
        
        # while len(stack) > 0:
        #     elem = stack[-1]
        #     if elem in graph and len(graph[elem]) > 0: 
        #         # Check if elem in graph as there may be a case when there is no out edge from an airport 
        #         # In that case it won't be present as a key in graph
        #         stack.append(graph[elem].pop())
        #     else:
        #         res.append(stack.pop())
        #         # If there is no further children to traverse then add that airport to res
        #         # This airport should be the last to go since we can't anywhere from this
        #         # That's why we return the reverse of the result
        # return res[::-1]

    """
    Neetcode solution 

    causing time exceeds error

    we can treat this as a dfs graph traversal problem
        the problem is to identify the order of airports to travel so that all the tickets would be used 
        they'd like the result in alphabetical order
        to achieve this we create an adjacency list & populate it
        before populating the adjacency list, sort the input, this'll take care of sending result in alphabetical order

    create an helper recursive dfs function
        check base conditions
            if length of result is equal to length of tickets input + 1
                since result length is always going to be equal to length of tickets + 1
            if src not in adjMap
                means this airport is a destination, there is no source flight from here
        
        now loop for the dest for this airport from adj list
            remove each dest airport from the list
            add the dest airport to result array
            call the function recursively
                if call response is true, a path is possibel & return true
            if not, add this dest airport back to list
            remove dest airport from result array
        return false in the end
    
    once all calls return, the itineray is in the result array
    """
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     # create adjacency list
    #     adjMap = {src: [] for src, des in tickets}

    #     tickets.sort()

    #     # populate adjMap
    #     for sr, des in tickets:
    #         adjMap[sr].append(des)
        
    #     # initialize result variable with JFK - since starting point
    #     res = ["JFK"]

    #     # helper function
    #     def dfs(src):
    #         # base condition
    #         # check if length of result equal to length of tickets + 1
    #         if len(res) == len(tickets) + 1:
    #             return True
    #         # check if this src airport doesn't exist in adjMap -- which means, there is no returning from this airport
    #         if src not in adjMap:
    #             return False
            
    #         # loop thru each destination for this src airport & recursively call
    #         tempList = list(adjMap[src])

    #         # loop thru 
    #         for i, airport in enumerate(tempList):
    #             # remove current airport from adjMap for this src -- for future considerations
    #             adjMap[src].pop(i)
    #             res.append(airport) # append to airport since visiting

    #             # recursive call for this aiport, if it returns True, we've found a path, return from function
    #             if dfs(airport): return True

    #             # reaches here if function call is not True, which means can't visit this airport now
    #             # add this airport back to adjMap
    #             adjMap[src].insert(i, airport)
    #             res.pop()
            
    #         # If none of the airports return True, then it can't be done, return False
    #         return False
        
    #     # initial func call with JFK -- since origin airport at all times
    #     dfs("JFK")

    #     # final return value
    #     return res