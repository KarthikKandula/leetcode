# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base condition
        # if input is empty
        if not nums:
            return None # return none
        
        # # get length of input
        n = len(nums)

        # get mid point of the array
        mid = n // 2

        # create root node with mid point
        root = TreeNode(nums[mid])

        # recursive call for left node
        root.left = self.sortedArrayToBST(nums[:mid])
        # recursive call for right node
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        # return root node
        return root
