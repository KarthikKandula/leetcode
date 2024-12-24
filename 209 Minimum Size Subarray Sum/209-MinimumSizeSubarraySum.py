class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 # left pointer
        total = 0 # to keep track of sum in current window
        res = len(nums) + 1 # max value possible for result -- helpful in min operations

        # loop thru input array with right pointer
        for r in range(len(nums)):
            # append current right pointer value to total
            total += nums[r]

            # while total is greater than or equal to target
            while total >= target:
                # get current length of window & get min value with existing result
                res = min(res, (r - l + 1))
                total -= nums[l] # deduct left pointer value from total
                l += 1 # increment left pointer

        # return result value if not equal to initialized value else return 0
        return res if res != len(nums) + 1 else 0
