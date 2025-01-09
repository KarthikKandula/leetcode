class Solution:
    def myAtoi(self, s: str) -> int:
        # strip any spaces before in the start & end
        s = s.strip()

        # after stripping check if string is empty
        if not s:
            return 0 # return 0

        # variable to determine sign
        sign = 1

        # extract sign from input
        if s[0] == '-': # if sign is -ve
            sign = -1
            s = s[1:] # update string to remove sign
        elif s[0] == '+': # if sign is +ve
            sign = 1 
            s = s[1:] # update string to remove sign
        
        # variable to record result
        res = 0

        # loop for each char in input
        for c in s:
            # if current value is not a char
            if not c.isdigit():
                break # break the loop

            # add current variable to our calculation
            res = (res * 10) + int(c)
        
        # update result with sign from above
        res *= sign

        # initialize int_min & int_max
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # check rounding
        # if result is within int min & max bounds
        if res >= INT_MIN and res <= INT_MAX:
            return res
        else: # if isn't, return appropriately
            return INT_MIN if res < 0 else INT_MAX
