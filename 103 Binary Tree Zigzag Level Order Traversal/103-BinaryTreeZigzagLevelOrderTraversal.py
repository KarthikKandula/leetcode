# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base condition - if root is empty, return empty array
        if not root:
            return []
        
        # to hold result
        res = []

        # create queue to perform bfs
        q = deque()

        # append root node to queue
        q.append(root)

        # create bool variable to track reverse levels
        zigzag = False

        # loop while q is initialized
        while q:
            # get length of queue for this level
            qLen = len(q)

            # array to store values at this level
            temp = []

            # loop for length of this level
            for i in range(qLen):
                # pop node from left
                node = q.popleft()

                # add node value to temp array
                temp.append(node.val)

                # if node has left node
                if node.left:
                    # append to queue
                    q.append(node.left)
                # if node has right node
                if node.right:
                    # append to queue
                    q.append(node.right)
            
            # if zigzag value is true, means we have to reverse the order
            if zigzag:
                # reverse temp array
                temp = temp[::-1]
            
            # append temp array to result
            res.append(temp)

            # negate zigzag value for next iteration
            zigzag = not zigzag

        # return result array
        return res
