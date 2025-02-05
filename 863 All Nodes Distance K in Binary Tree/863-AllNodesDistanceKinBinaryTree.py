# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    this is a basic/simple bfs traversal in disguise
        finding nodes at k distance is easy in a graph
            but the input is a binary tree
        so convert binary tree to a graph (undirected graph)
            and apply bfs to find nodes at k distance, gets easy
    """
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # create graph
        graph = defaultdict(list)

        # recursive function to populate graph
        def populateGraph(curr):
            # if curr is null, do nothing
            if not curr:
                return

            # if node has left node
            if curr.left:
                # add to graph similar to an undirected node
                graph[curr.val].append(curr.left.val)
                graph[curr.left.val].append(curr.val)

                # recursive call to left node
                populateGraph(curr.left)

            # if node has right node
            if curr.right:
                # add to graph similar to an undirected node
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val].append(curr.val)

                # recursive call to right node
                populateGraph(curr.right)

        # call to populate graph w/ root
        populateGraph(root)

        # apply bfs to find nodes at k distance

        # create queue
        q = deque()
        q.append(target.val) # insert target node value to kickstart algo

        level = 0 # track level in bfs search
        visited = set() # to track visited nodes
        # res = []

        # loop while q is populated
        while q:
            # get length of queue in current level
            qLen = len(q)

            # if current level is equal to k
            if level == k:
                # return elements in queue
                return list(q)

            # loop for current queue length
            for i in range(qLen):
                # pop left most node
                node = q.popleft()

                # add curr node to visited -- to avoid infinite loops
                visited.add(node)

                # if level == k:
                #     templist.append(node)

                # get all neighbors for this node from graph
                for nei in graph[node]:
                    # if this nei is not yet visited
                    if nei not in visited:
                        # append to queue
                        q.append(nei)

            # if level == k:
            #     res = templist
            #     break

            # increment level
            level += 1

        # return empty list if didn't return in loop
        return []
