class Solution:
    """
    we can treat this as a graph traversal problem
        we can create a graph for every node & edge given in the problem
        the goal is to get the no. of connected graphs in the input
        an added logic to notice is that this is an undirected edges between nodes
        so to counteract the undirectd nature, we add the nodes to each node on either side of the edge
        the entire logic is based out of the visited set
            checking if a node is in visited set 
            incrementing result variable only if it isn't

    create a hashmap with every node & populate the connections for each course
        since undirected, need to populate for either side of the edge
    create a set to take note of visited nodes already -- helps in detecting cycles

    create a helper function to implement recursively
        input is a node

        loop thru all surrounding node's this node has
            check if the current neighbor node is in visited
                if it isn't, do below
                add node to visited
                recusively call each neighbor
    
    loop thru range(n) to call recursive function for all nodes
        check if the current node is in visited
            if it isn't, do below
            add node to visited
            recusively call each neighbor
            increment result variable
    
    by the time all nodes have been called, result is in the variable
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create a adjacency list to save connections for each node
        adjMap = {i:[] for i in range(n)}

        # create a result variable
        res = 0

        # # Loop thorugh input edges - to populate hashmap
        for a, b in edges:
            # appending to each node, since it's an undirected graph
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        # Create a set to track visited nodes
        visited = set()

        # helper function to implement recursively to visit all nodes
        def dfs(node):
            # no need to do a base condition check since we're doing that in loop 
                # only calling functions if they are not in visited

            # loop thru each neighbor for this node
            for eachNei in adjMap[node]:
                # check if this node has already been visited
                if eachNei not in visited:
                    visited.add(eachNei) # add node to visited -- since visiting now
                    dfs(eachNei) # recursive call for this node
        
        # loop thru each node in range(n)
        for eachNode in range(n):
            # check if this node has already been visited -- only call func if it's not yet visited
            if eachNode not in visited:
                visited.add(eachNode) # add node to visited -- since visiting now
                dfs(eachNode) # recursive call for this node
                res += 1 # increment result since we found an unvisited node aka graph
        
        # return result value
        return res
