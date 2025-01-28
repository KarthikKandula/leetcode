# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    this problem can be solved using a variation of prefix sum
        usually used to identify problem types like
        Find a number of continuous subarrays/submatrices/tree paths that sum to target
        the basic idea is that
            maintain a continous value of sum until now
            for each sum, at each location, add sum to hashmap
            check if the continous value - target value exists in the hashmap
                if it does, it means by removing those combinations, we can get to target
                increment count by the value of diff from hashmap
                    means, those many ways we can form the total by removing combinations
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # create a hashmap to record values seen before
        hashmap = defaultdict(int)
        self.res = 0 # variable to count no. of paths till now

        # recursive dfs function
        def dfs(node, total):
            # base conditions
            # if node is null, return w/o doing anything
            if not node:
                return
            
            # add this node's value to total
            total += node.val

            # if total until now is equal to target sum
            if total == targetSum:
                self.res += 1 # increment count value

            # check if the difference to targetSum exists in hashmap
            # it means, by removing those values, we can get a collection of nodes that sum up to targetSum
            self.res += hashmap[total - targetSum] # add the no. of times that is possible
            
            # increment the count for this total
            # after adding diff value to result, to not interfere with those calculations
            hashmap[total] += 1

            # call for left & right nodes
            dfs(node.left, total)
            dfs(node.right, total)

            # decrement the count for this total
            # since dfs, to not interfere with parallel subtree validation
            hashmap[total] -= 1

        # initial call 
        dfs(root, 0)

        # return result value
        return self.res

    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
    #     hashmap = {}
    #     res = 0

    #     def dfs(node, total):
    #         # base conditions
    #         if not node:
    #             return
            
    #         total += node.val

    #         if total == targetSum:
    #             print(f"{node}, {total}")
    #             self.res += 1
            
    #         # include current node
    #         # left
    #         dfs(node.left, total)
    #         # right
    #         dfs(node.right, total)

    #         # don't include current node
    #         # left
    #         dfs(node.left, 0)
    #         # right
    #         dfs(node.right, 0)

    #         return 
        
    #     dfs(root, 0)

    #     return self.res
