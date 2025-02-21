class Solution:
    """
    we can solve this problem using binary search
        basically check for each number from 0...x to see which value is the square root
        to make this more efficient, we can use binary search
            with each calculation, eliminate half of the values
            the highest value where the square root is less than target is the result
                unless an exact root has been found
    """
    def mySqrt(self, x: int) -> int:
        # create left & right pointers
        l, r = 0, x

        # result variable
        res = 0

        # loop while left & right pointers haven't crossed each other
        while l <= r:
            # m = (l + r) // 2 # regular mid logic
            m = l + ((r - l) // 2) # mid logic to avoid overflow error

            # check if square of this number is greater than x
            if m * m > x:
                # eliminate right half
                r = m - 1
            # check if square of this number is less than x
            elif m * m < x:
                # get max result
                res = max(res, m)
                # eliminate left half
                l = m + 1
            # if number is the exact same
            else:
                # return current mid value
                return m

        # return result value
        return res
