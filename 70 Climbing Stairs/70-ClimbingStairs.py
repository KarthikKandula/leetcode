class Solution:
    """
    Memoized recursive approach

    this implements the same regular recursive approach but elimates a layer of recursive function calls

    take an array initialized to -1 for the length of input n
        -1 indicates this value isn't yet calculated
    
    now in a function call before making recursive calls
        check if the array has been initialized at this index
        if it is, return the value -- reducing the amount of function calls by reusing them effectively
    """
    def climbStairs(self, n: int) -> int:
        # create an array with default -1 values for length of n
        cache = [-1] * n

        # recursive function
        def dfs(i):
            # check if input index is equal to n -- i.e, target reached
            if i == n:
                return 1 # return 1 -- to indicate a way
            # if input is greater than n -- i.e, target overshot
            if i > n:
                return 0 # return 0 -- to indicate this is not a way
            
            # check if cache array has a value for this index
            if cache[i] != -1:
                return cache[i] # if it does, return that value -- reusing values to avoid making more function calls
            
            # save recursive function return values to cache
            cache[i] = dfs(i + 1) + dfs(i + 2)

            # return value from cache
            return cache[i]

        # return value
        return dfs(0)

    """
    Regular recursive approach

    we can use regular recursion to solve the problem
    
    create a helper function to implement recursively
        input is the stair num
        check base conditions
            if input equal to n 
                target is reached
                return 1 to signify a way has been found
            if input is greater than n
                target is overshot
                return 0 to signify this is not a way
        
        recursively call stair + 1 and stair + 2
            return their added value
    
    return the return value of first function call for index 0
    """
    # def climbStairs(self, n: int) -> int:

    #     # recursive function
    #     def dfs(i):
    #         # check if input index is equal to n -- i.e, target reached
    #         if i == n:
    #             return 1 # return 1 -- to indicate a way
    #         # if input is greater than n -- i.e, target overshot
    #         if i > n: 
    #             return 0 # return 0 -- to indicate this is not a way

    #         # return addition of 1 step + 2 steps
    #         return dfs(i + 1) + dfs(i + 2)
        
    #     # first recursive call
    #     return dfs(0)

