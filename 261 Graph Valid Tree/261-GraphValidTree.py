class Solution:
    """
    we can treat this problem as a graph traversal problem
        we can create a graph for every node & edge given in the problem
        the goal is to make sure we can take every node is connected & there are no cycles
        an added logic to notice is that this is an undirected edges between nodes
        so to counteract the undirectd nature, we add the nodes to each node on either side of the edge
        and record the previous node/calling parent node to ignore recursive call for that node

    create a hashmap with every node & populate the connections for each course
        since undirected, need to populate for either side of the edge
    create a set to take note of visited nodes already -- helps in detecting cycles

    create a helper function to implement recursively
        input is a node & calling parent node
        if node is in visited
            return False
        
        if reaches this point, it means this is a new node we're visiting & should be validated
        add node to visited
        loop thru all surrounding node's this node has & recusively call each course
            since this is an undirected graph, we need to skip the parent node
                compare if current node is parent, then skip it
            if any node returns false, return false for entire function
        
        if reaches this point, it means no course returned false
        return True

    in the end, return the return value of first func call & if length of visited is equal to the no of nodes
        to make sure there are no nodes that aren't connected to graph
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create a adjacency list to save connections for each node
        adjMap = {i:[] for i in range(n)}

        # Loop thorugh input edges - to populate hashmap
        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)

        # Create a set to track visited nodes
        visited = set()

        # helper function to implement recursively to check cycles & visit all nodes
        def dfs(node, prevNode):
            # If current node is already in visited, it means there is a loop
            if node in visited:
                return False
            
            # If gets to this point, this node has not been visited
            # Add this node to visit
            visited.add(node)

            # loop thru surrounding nodes
            for eachNode in adjMap[node]:
                # if eachNode is the calling node - skip that node
                if eachNode == prevNode:
                    continue
                
                # recursively call for each connected node -- if the response is False for any node
                if not dfs(eachNode, node):
                    return False # return False, since there's a cycle

            # return True, since there are no cycles for the current node
            return True
        
        # return return value of first recursive func call & if the length of visited set == input n
        # if the length of visited set == input n -- to make sure there are no nodes that aren't connected to graph
        return dfs(0, -1) and len(visited) == n