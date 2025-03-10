# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Declare queue & result
        q, res = deque(), 0
        
        # Initialize queue with root value
        q.append(root)

        # loop while queue has values
        while q:
            # pop from queue
            cur = q.popleft()
            
            # if popped value is none, skip that value
            if not cur:
                continue

            # check if this popped value is within low & high
            if low <= cur.val <= high:
                # if yes, add to result
                res += cur.val

            # check if popped value is lower than low value
            if cur.val <= low:
                # only valid values are in right sub-tree, only explore that
                q.append(cur.right)
            # check if popped value is higher than high value
            elif cur.val >= high:
                # only valid values are in left sub-tree, only explore that
                q.append(cur.left)
            # if popped value is within bounds
            else:
                # valid values might be in both sub-tree's, explore both
                q.append(cur.left)
                q.append(cur.right)

        # return result array
        return res
