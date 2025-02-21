class Solution:
    """
    without modifying input
    """
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # cover edge case, if input is empty
        if not nums:
            # return list of lower & upper
            return [[lower, upper]]

        n = len(nums) # get length of input, to avoid repeated calculations
        res = [] # create result array
        prev = lower - 1 # initialize prev value to lower

        # loop thru input
        for i in range(len(nums) + 1):
            # get value at current index, if last index, get upper + 1
            curr = nums[i] if i < n else upper + 1

            # check if there are elements between prev vlaue & this value
            if prev < curr - 1:
                # if there is, append the interval between
                res.append([prev + 1, curr - 1])
            
            # reassign curr to prev -- for next iteration
            prev = curr
        
        # return result array
        return res

    """
    Modifying input
    """
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # cover edge case, if input is empty
        if not nums:
            # return list of lower & upper
            return [[lower, upper]]

        # if first value isn't equal to lower
        if nums[0] != lower:
            # add lower at first index to input
            nums.insert(0, lower - 1)
        # if last value isn't equal to upper
        if nums[-1] != upper:
            # append upper at the last
            nums.append(upper + 1)

        # create result array
        res = []

        # loop thru input
        for i in range(1, len(nums)):
            # check if there are elements between prev vlaue & this value
            if nums[i - 1] < nums[i] - 1:
                # if there is, append the interval between
                res.append([nums[i - 1] + 1, nums[i] - 1])

        # return result array
        return res
