# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    use basic level order traversal i.e, bfs to solve this problem
        the problem is to identify the last value in a level in a binary tree
    
    we use level order traversal's characteristics to our advantage
    since in level order traversal, we go thru the tree based on levels
    we create an inner loop after each level has completed so we go thru each level's values seperate

    take an empty output array
    take a queue -- used for bfs

    loop while queue is not empty
        get the queue's length at that point -- that is the no. of node's at that level
        create an inner loop & go thru the queue for queue's length from before
            pop from queue
            check if that node is the last at that level -- add to output array
            add left & right nodes to queue

    in the end, return output array
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if root is empty
        if not root:
            return [] # return empty array

        # queue to implement bfs -- using bfs
        queue = [root]
        out = [] # output array

        # loop while queue is non empty
        while queue:
            # get queue's length -- for inner loop for current level
            qLen = len(queue)

            # loop for current level
            for i in range(qLen):
                # pop first node
                tempNode = queue.pop(0)

                # check if node has a left node
                if tempNode.left:
                    queue.append(tempNode.left) # append to queue
                # check if node has a right node
                if tempNode.right:
                    queue.append(tempNode.right)  # append to queue
                
                # check if current node is last at current level
                if i == qLen - 1:
                    out.append(tempNode.val) # append value to out

        # return out array
        return out
