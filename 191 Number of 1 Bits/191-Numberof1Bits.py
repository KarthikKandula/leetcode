class Solution:
    """
    the idea behind this is to bit & the number n to n - 1
        by doing this, we'll be slowly removing all 1's in the number
        and since it's an and(&) operation, any 1's that have any mismatches will be made to 0's
        the pro in this method is that the loop won't run 32 times (since 32 bit integer)
            once all the values are 0, loop will stop
    """
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            n = n & (n - 1)
            res += 1

        return res

    """
    the idea is to apply % 2 to the number before right shifting bits by 1
        by doing % 2
            if there is a 1 in the end, remainder is 1, which will be added to result
            if there is a 0 in the end, remainder is 0
        by shifting bits right by 1
            we're moving all values to the right, so once the % operation is done we'll be getting the next value
        

    loop only stops once all 1's have been visited & the number turns to 0
        in the worst case, this loop would run 32 times (since 32 bit integer)
    """
    # def hammingWeight(self, n: int) -> int:
    #     res = 0

    #     while n:
    #         res += n % 2
    #         n = n >> 1
        
    #     return res
