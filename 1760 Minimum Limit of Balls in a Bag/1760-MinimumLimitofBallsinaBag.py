class Solution:
    """
    the idea is to 
        check for each possible value if it's possible to divide all values in input nums
        the lowest value that it's possible to divide is the result

        to achieve this, we take the max number in nums & try to check for each number from 1...maxval
        an efficient way to do this is to use binary search, so we halve the no. of checks
    """
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        # create helper function to check if it's possible to atleast divide all bags into max_balls bags within max ops
        def sizeHelper(max_balls):
            ops = 0 # variable to get total no. of operations for this max_balls value

            # loop for each nums value
            for n in nums:
                # divide each number with max_balls & subtract 1 -- since it already exists
                # we're checking the no. of ops it takes on a single ball to reduce it to max_balls
                ops += ceil(n / max_balls) - 1

                # if the no. of ops is greater than maxOps at any time -- it's not possible for this max_balls value
                if ops > maxOperations:
                    return False # return False

            # return true
            return True

        # create left & right pointers for binary search
        l, r = 1, max(nums)

        res = r # result variable

        # loop while left is less than r
        while l < r:
            # calculate mid value
            mid = (l + r) // 2

            # call helper function to see if it's possible to divide into this mid value
            if sizeHelper(mid):
                # if it is possible, reassign the right pointer to mid to try using a lower value
                # since asked for min possible balls
                r = mid
                res = r # update result with current value since it's possible to divide all bags for this number
            else:
                # it's not possible, try with a higher number
                l = mid + 1

        # return result value, last & least possible value
        return res
