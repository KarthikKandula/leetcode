class Solution:
    """
    the idea behind this is to use values previously calculated to count future values
        the way bit operations work is patterns repeat for every base 2 levels (1,2,4,8 etc.,)
        so by reusing the value previously calculated & adding 1 to it, we get the new 1's count

        by doing this we're solving the problem in single pass
    """
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp

    """
    Loop thru each number from 0 to n & perform & for n & n - 1

    the idea behind this is to bit & the number n to n - 1
        by doing this, we'll be slowly removing all 1's in the number
        and since it's an and(&) operation, any 1's that have any mismatches will be made to 0's
        the pro in this method is that the loop won't run 32 times (since 32 bit integer)
            once all the values are 0, loop will stop
    """
    # def countBits(self, n: int) -> List[int]:
        
    #     res = []

    #     for i in range(n + 1):
    #         out = 0

    #         temp = i

    #         while temp:
    #             temp = temp & (temp - 1)
    #             out += 1

    #         res.append(out)
        
    #     return res
