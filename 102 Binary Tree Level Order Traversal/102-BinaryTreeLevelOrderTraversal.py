# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    we can use basic level order traversal i.e, bfs to solve this problem
        the problem is to identify values by level in a binary tree
    
    we use level order traversal's characteristics to our advantage
        since in level order traversal, we go thru the tree based on levels
        we create an inner loop after each level has completed so we get each level's values seperate
    
    take an empty output array
    take a queue -- used for bfs

    loop while queue is not empty
        create an empty temp array for that level
        get the queue's length at that point -- that is the no. of node's at that level
        create an inner loop & go thru the queue for queue's length from before
            pop from queue
            add value to level array
            add left & right nodes to queue
        after inner loop has exited, add level to output -- we got all the values at that level
    
    in the end, return output array
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root is null, return empty array
        if not root:
            return []

        # create an output variable
        out = []

        # queue for implementing bfs
        queue = [root]

        # loop while queue is non-empty
        while queue:
            # initialize empty array to store this level's values
            level = []
            # get queue length for this level -- to run inner loop
            qLen = len(queue)

            # loop until qLen -- getting this level values & adding any new nodes to queue
            for i in range(qLen):
                # pop first value in queue -- standard in bfs
                tempNode = queue.pop(0)

                # append tempNode's value to level
                level.append(tempNode.val)

                # check if tempNode has a left node
                if tempNode.left: 
                    queue.append(tempNode.left) # insert into queue
                # check if tempNode has a right node
                if tempNode.right: 
                    queue.append(tempNode.right) # insert into queue

            # check if level has values -- don't want empty arrays in output
            if level:
                out.append(level)

        # return out
        return out