class Solution:
    """
    we can treat this as a cycle detection problem in an undirected graph
        given a list of edges, we aim to identify the redundant edge that forms a cycle
        the goal is to find the first edge that creates a cycle when added to the graph
    
    create two arrays, parent and rank, for Union-Find (Disjoint Set Union) operations
        parent array tracks the root parent of each node, initialized with each node as its own parent
        rank array tracks the size of each tree, initialized with rank 1 for each node

    create a helper function `find` to locate the root of a node
        this function implements path compression
        by updating each node's parent to point directly to the root, it optimizes future calls

    create a helper function `union` to connect two nodes
        this function implements union by rank to keep trees balanced
        it returns False if the nodes are already connected (indicating a cycle) and True otherwise
    
    loop through each edge in the input
        for each edge, attempt to union the two nodes
        if union fails, it means the edge creates a cycle, so return this edge
    
    by the end of the loop, the first cycle-causing edge is returned as the redundant connection
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create parent array -- every node is parent to itself
        parent = [i for i in range(len(edges) + 1)]
        # create rank array -- every node has rank 1 
        rank = [1] * (len(edges) + 1)

        # helper function to find parent of a node
        def find(n):
            # get n's parent
            p = parent[n]

            # loop while parent is not equal to itself
            while p != parent[p]: # While `p` is not its own parent
                # get granfather of current node
                parent[p] = parent[parent[p]] # Path compression step
                # # Move `p` up one level
                p = parent[p]
            
            # return parent p
            return p
        
        # helper function to create union of two nodes
        def union(n1, n2):
            # get root nodes for n1 & n2
            r1, r2 = find(n1), find(n2)

            # if both root nodes are same -- it means they're already connected
            if r1 == r2:
                return False # Cycle detected, since `n1` and `n2` are already connected
            
            # Union by rank
            # `r1` has a larger tree, so attach `r2` to `r1`
            if rank[r1] > rank[r2]:
                parent[r2] = r1 # assign r1 as parent to r2
                rank[r1] += rank[r2] # increment r1's rank to indicate the increase in depth
            else: # Attach `r1` to `r2`
                parent[r1] = r2 # assign r1 as parent to r2
                rank[r2] += rank[r1] # increment r2's rank to indicate the increase in depth

            # return True since a connection is possible
            return True

        # iterate thru edges
        for a, b in edges:
            # if union func returns false for any edge -- it means they're already connected
            if not union(a, b):
                return [a, b] # return that edge
        
        # no need to return anything here, since an extra connection will exist