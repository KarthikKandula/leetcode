class Solution:
    """
    NeetCode Optimal solution

    the advantage with dealing with power operations is 
        2^32 = 2^16 * 2^16
        so if we calculate 2^16 value once, we can multiply it with itself to get 2^32 value
        we use this to our advantage essentially reducing the no. of operations 
        so time complexity if O(log n)
    """
    def myPow(self, x: float, n: int) -> float:
        def helper(num, p):
            # base conditions
            # if number is equal to 0
            if num == 0:
                return 0 # return 0
            # if power is 0, answer is 1
            if p == 0:
                return 1 # return 1
            
            # multiply a value by itself to reduce the no. of iterations in half
            # while making the next function call, multiply this value by itself while halfing power value
            # making this operation log n time
            res = helper(num * num, p // 2)
            # multiply number once more if power is an odd number else return result
            return num * res if p % 2 else res
        
        # initial call to recursive function
        out = helper(x, abs(n))
        # return recursive function output based on neg/pos power value
        return out if n >= 0 else 1 / out

    """
    My solution
    """
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 1:
    #         return x * n
    #     if n == -1:
    #         return 1 / (x * abs(n))
        
    #     if n < 0:
    #         return (1 / x) * self.myPow(x, n + 1)

    #     return x * self.myPow(x, n - 1)