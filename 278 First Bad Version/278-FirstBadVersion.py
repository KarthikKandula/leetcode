# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # left & right pointer on either end
        l, r = 1, n

        # variable to track badversion, need the min, so assigning to the max
        badVersion = n

        # loop while left is less than r
        while l <= r:
            # calculate mid value
            m = (l + r) // 2

            # if current mid is not bad
            if not isBadVersion(m):
                l = m + 1 # move left pointer
            else: # if current mid is bad
                # get the min bad version
                badVersion = min(badVersion, m)
                r = m - 1 # move right pointer

        # return bad version
        return badVersion

