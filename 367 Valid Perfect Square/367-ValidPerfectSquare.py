class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # left & right pointers
        l, r = 0, num

        # loop while left & right doesn't cross
        while l <= r:
            # calc mid value 
            m = l + ((r - l) // 2) # to avoid overflow 

            # squre mid value
            midSquare = m * m

            # if mid square value is greater than num
            if midSquare > num:
                # can eliminate right half
                r = m - 1 # move right pointer back
            # if mid square value is less than num
            elif midSquare < num:
                # can eliminate left half
                l = m + 1
            # if mid square value is same as num
            else:
                # found value
                return True
        
        # if return isn't triggered above, return False
        return False
