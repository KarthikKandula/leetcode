class Solution:
    """
    NeetCode solution

    the idea is to
        get each digit from one's place by using remainder operation
        update x by dividing with 10, to remove above digit

        check if until that point result value has a chance of overflowing
            check if it's greater than the MAX value & is it going to be greater than max value after adding current digit
            same with MIN
        
        if not going to overflow, add to result & repeat loop
    
    in the end return result value
    """
    def reverse(self, x: int) -> int:
        # create variables holding MIN & MAX values
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        # result variable
        res = 0

        # loop while x has a value
        while x:
            # get the digit in ones place
            digit = int(math.fmod(x, 10))
            x = int(x / 10) # update x to remove value in one's place

            # check if res is overflowing above MAX
            if (res > MAX // 10) or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            # check if res is overflowing below MIN
            if (res < MIN // 10) or (res == MIN // 10 and digit <= MIN % 10):
                return 0

            # update res
            res = (res * 10) + digit

        # return res
        return res

    """
    My solution
    """
    # def reverse(self, x: int) -> int:
    #     flag = True if x < 0 else False

    #     x = abs(x)

    #     num = int(str(x)[::-1])

    #     if flag:
    #         num *= -1
        
    #     # if num < -(1 << 31) or num > (1 << 31) - 1:
    #     #     return 0
        
    #     if num < (-2 ** 31) or num > (2 ** 31) - 1:
    #         return 0

    #     return num

