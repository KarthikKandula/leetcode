class Solution:
    """
    we can solve this problem using prefix sum
        subtract 1 from prefix sum for every 0 value
        add 1 to prefix sum for every 1 value
        the idea is a prefix sum value appears again in the array
            it means between the last location & the new location there are same num of 0 & 1 
            get the max value of existing output value & the new window
        if at any point prefix sum becomes 0
            update the max value with current index 
            since only happens if there are same num of 0 & 1
    """
    def findMaxLength(self, nums: List[int]) -> int:
        preSum = 0 # to hold prefix sum
        hashmap = {} # hashmap to save prefix sum & their index
        out = 0 # to store output value -- max contiguous subarray

        # loop thru input nums
        for i, v in enumerate(nums):
            # add 1 if val is 1 or -1 if val is 0
            preSum = preSum + 1 if v == 1 else preSum - 1

            # if this prefix sum isn't in hashamp, add to hashmap with curr index
            if preSum not in hashmap:
                hashmap[preSum] = i

            # get the last appeared location for this prefix sum & subtract with index to get current max
            # get max out of already max
            out = max(out, i - (hashmap[preSum]))

            # if the prefix sum is 0, only happens if there are same no. of 0 & 1
            if preSum == 0:
                out = max(out, i + 1) # get the max of curr max & curr index

        # return output value
        return out
