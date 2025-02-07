class Solution:
    """
    if we observer the problem description closely
        we realize that same numbers take the same no. of operations
        different numbers almost always take different no. of operations
        the answer is the no. of unique values other than 0
    """
    def minimumOperations(self, nums: List[int]) -> int:
        # create a set with nums & remove 0 from the values
        nums = set(nums) - {0}

        # return the length of newly formed set
        return len(nums)
