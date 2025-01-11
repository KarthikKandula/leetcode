class Solution:
    """
    we can solve this using two pointers
        the solution for this question is simple
        after understanding the input parameters, they are in non-decreasing order
        so the max value is always going to come from one of either ends
        take two pointers on either side
            square the bigger value & append to end of result array
        once it reaches 0th index, all values are populated
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointers on opposite side of input
        l, r = 0, len(nums) - 1

        # create output array
        out = [0] * len(nums)

        # loop thru input in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # check which absolute value is greater
            # if left is greater than right
            if abs(nums[l]) >= abs(nums[r]):
                # calcuate square & save in ith location
                out[i] = nums[l] * nums[l]
                l += 1 # increment l pointer
            else: # if right is greater than left
                # calcuate square & save in ith location
                out[i] = nums[r] * nums[r]
                r -= 1 # increment r pointer

        # return output array
        return out
