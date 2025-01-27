# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # variable to store result
        res = 0

        # create queue to implement bfs
        q = deque()
        q.append((root, 1)) # add root & value 1 to queue to kickstart bfs

        # loop while q is valid
        while q:
            # get length of queue for this level
            qLen = len(q)

            levelMin = q[0][1] # get lowest node's level value            
            levelMax = q[qLen - 1][1] # get highest node's level value

            # compute result value & get the max
            res = max(res, (levelMax - levelMin) + 1)

            # loop for current level to add all child nodes for nodes in this level
            for i in range(qLen):
                # pop from right
                node, level = q.popleft()

                # if node has left child
                if node.left:
                    q.append((node.left, (level * 2) - 1))
                # if node has right child
                if node.right:
                    q.append((node.right, level * 2))

        # return res
        return res
