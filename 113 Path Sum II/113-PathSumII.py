# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # if root is null
        if not root:
            return [] # return empty array

        # create result array
        res = []
        subset = [] # create subset array

        def dfs(cur, count):
            # base conditions
            
            # append current node value to count
            count += cur.val

            # append this value to subset
            subset.append(cur.val)

            # check if this node satisfies all conditions
            if count == targetSum and not cur.left and not cur.right:
                # if it does, add subset copy to result array
                res.append(subset.copy())

            # if this node has left subtree
            if cur.left:
                # recursive call for left subtree
                dfs(cur.left, count)
            # if this node has right subtree
            if cur.right:
                # recursive call for right subtree
                dfs(cur.right, count)

            # pop from subset -- cleanup subset
            subset.pop()

            # return from function
            return

        # initial recursive call
        dfs(root, 0)

        # return result array
        return res
