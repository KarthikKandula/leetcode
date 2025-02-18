class Solution:
    """
    O(1) solution

    Use two pointers to solve the problem
        start with initial values 0 & 1 -- they're constant
        use these two to build the values from there
    """
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev = 0 # fib value for 0
        cur = 1 # fib value for 1

        i = 2 # start loop from fib(2)

        # loop while i is less than n
        while i <= n:
            # take backup of current value
            bckup = cur

            # add prev & cur value to form a new value
            cur = cur + prev
            prev = bckup # assign cur to prev -- for next iteration

            i += 1 # increment i value

        # return cur
        return cur

    """
    Top-Down Recursive solution

    Use recursion/dp with memoization to solve this problem
        use cache to store values instead of performing the same calculations multiple times
        once a value has been calculated, save it to the cache, for faster access next time
    """
    def fib(self, n: int) -> int:        
        if n <= 1:
            return n

        # create cache for lenght of n
        cache = [-1] * (n + 1)
        cache[0] = 0 # create base value 
        cache[1] = 1 # create base value 

        # recursive function 
        def calcFib(i):
            # base conditions
            # if value is in cache, return from cache
            if cache[i] != -1:
                return cache[i]

            # calculate current value & save to cache 
            cache[i] = calcFib(i - 1) + calcFib(i - 2)

            # return value from cache
            return cache[i]
        
        # return value of first function call is returned out
        return calcFib(n)
