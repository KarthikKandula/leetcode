class Solution:
    """
    this problem can be solved using a dfs graph traversal
        we need to find connected components between emails
        if we think of emails as nodes, then the connections between them determines if they belong to the same user
        so while building an adjacency list, we use the first email as a base node
            something to base the connections out of
            we can't use the user since there can be multiple different users with same name
            we'll use the first email here but we can use any email in the list
                serves the same purpose
        after building the adjacency list, we need extract common connections based on our list
            let's implement a dfs graph traversal algo with post-order traversal
            call the recursive function for each email in input & build an array of connected components for each
            keep a visited set handy to avoid loops & duplicate outputs
        recursive function
            add the current node to visited
            loop for each neighbor in the adjacency list & call for neighbor
            once all neighbors are visited, add to result (post order traversal)
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create a graph
        graph = defaultdict(set)

        # build graph
        # loop for each account in accounts
        for account in accounts:
            # loop for each email in account -- from 1st index
            for email in account[1:]:
                # append each email to first account to establish a base node
                graph[account[1]].add(email)
                # append first account to each email to establish connections, since it's an undirected graph
                graph[email].add(account[1])
        
        # implement dfs
        # set to track visited nodes
        visit = set()
        out = [] # output array

        # recursive function to implement dfs
        # visits all nodes & add to result array in post order traversal
        def dfs(result, node):
            # add node to visited
            visit.add(node)
            
            # visit all neighbor nodes
            for nei in graph[node]:
                # if this nei is not in visited node
                if nei not in visit:
                    # save return result to result array
                    # sending result array to get the updated array
                    result = dfs(result, nei)
            
            # add node if everything is visited to result
            # add current node to result since all nei's have been visited
            result.append(node)

            # return result array -- indicates all connected components to this node
            return result

        # loop for each account
        for account in accounts:
            # loop for each email in accounts
            for email in account[1:]:
                # if email is not in visited, skip
                if email not in visit:
                    # call recursive function with empty result set add emails to this res
                    res = dfs([], email)

                    # append output array using name from first place & sort result array as per prob des
                    out.append([account[0]] + sorted(res))

        # return output array
        return out
