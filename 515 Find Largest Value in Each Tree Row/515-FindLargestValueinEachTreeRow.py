# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # if input root doesn't have any nodes
        if not root:
            return [] # return empty array

        # create a queue
        q = deque()
        q.append(root) # append root to queue

        # create output array
        out = []

        # loop while q is initialized
        while q:
            # get length of queue
            qLen = len(q)
            # create variable to track max number for this level
            maxNo = q[0].val

            # loop for current length of queue
            for i in range(qLen):
                # pop from queue
                node = q.popleft()

                # update max value
                maxNo = max(maxNo, node.val)

                # add left, right to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # insert max val into output array
            out.append(maxNo)

        # return output array
        return out
