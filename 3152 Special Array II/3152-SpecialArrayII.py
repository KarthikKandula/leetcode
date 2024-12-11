class Solution:
    """
    the idea is to make the solution faster by 
        precalculating the mismatches until that point from start by checking
            if there are any odd & even's side by side
            increment that index's value by 1
            also carry on the value for each index & add 1 if there is a mismatch at that location
        
        while comparing from the queries
            the difference of from & to values from count array should be 0
                it indicates there are no adjacent odd & even values
            if diff is not 0, append False to result array
    """
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # create count array for the length of nums
        count = [0] * len(nums)

        # populate count array with mismatches in each location
        for i in range(1, len(nums)):
            # assign previous value to current value
            count[i] = count[i - 1]

            # check if there are any adjacent odd or even numbers
            if (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0) or (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0):
                # increment count since found another mismatch
                count[i] += 1

        # create array to store result
        res = []

        # loop thru each query to check if no. of mismatches are the same
        for frm, to in queries:
            # get the difference of mismatches btwn to & frm
            diff = count[to] - count[frm] # if count[frm] > 0 else 0)
            res.append(diff == 0) # append True/Flase to result array depending on if diff is 0

        # return result array
        return res

    """
    My solution
    """
    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
    #     res = [False] * len(queries)

    #     for i in range(len(queries)):
    #         frm, to = queries[i]

    #         lastParity = -1
    #         parityFlag = True
    #         for j in range(frm, to + 1):
    #             parity = nums[j] % 2
    #             if parity == lastParity:
    #                 parityFlag = False
    #             lastParity = parity

    #         # update value from result
    #         if parityFlag:
    #             res[i] = True

    #     return res
