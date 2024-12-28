class Solution:
    """
    this problem is similar to 3Sum
        we need to calculate sum of 3 different values from an array
        the twist is we need to keep track of the closest value
            return the closest value if actual target is not attainable
        to keep track of the lowest diff, create a variable
            this variable will be updated when we finf a new low diff
            and the result variable will also be updated
        rest of the logic is 3Sum
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort input for better comparision logic
        nums.sort()

        # variable to keep track of lowest difference
        diff = float('inf')
        res = 0 # variable to keep track of closest 3Sum

        # loop thru each value
        for k in range(len(nums)):
            # assign i & j pointers for numbers other than k
            i, j = k + 1, len(nums) - 1

            # loop while i < j -- standard two pointer logic
            while i < j:
                # calculate total sum for this iteration
                total = nums[k] + nums[i] + nums[j]

                # if total == target, end early by returning the total
                if total == target:
                    return total
                # if the difference to target is less than difference before
                elif abs(total - target) < diff:
                    # update diff value to new lowest diff value
                    diff = abs(total - target)
                    res = total # reassign result variable to new total value

                # logic to move pointers
                if total < target:
                    i += 1                
                else:
                    j -= 1

        # return result value
        return res


