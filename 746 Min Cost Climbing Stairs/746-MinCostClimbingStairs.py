class Solution:
    """
    Recursion w/ memoization

    we can treat this as a dynamic programming problem with memoization
        each step has a cost, and we want to reach the top with the minimum total cost
        at each step, we decide whether to move one or two steps forward, accumulating the minimum cost

    create a cache array to store intermediate results
        initialize the cache with -1 values, indicating uncomputed states
        cache stores the minimum cost to reach the top from each step, reducing redundant calculations

    define a recursive helper function `dfs` to calculate the minimum cost to reach the top
        input is the current step index (i)

        check if the step index has reached or exceeded the end of the cost array
        if it has, return 0 as no cost is needed beyond the last step
        check if the cache already has a computed value for this step
        if it does, return that cached value to avoid recalculating

        calculate and store the result in cache
        the minimum cost at step i is the cost of the current step plus the minimum of the costs of the next two steps

    call the helper function starting from the first two steps
        take the minimum of starting from step 0 and step 1 as the final result
        this gives the minimum cost to reach the top of the stairs
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # create an array with default -1 values for length of cost
        cache = [-1] * len(cost)

        # recursive function
        def dfs(i):
            # check if input index is equal to or greater than len(cost) -- i.e, the target has been reached
            if i >= len(cost):
                return 0 # return 0, since the cost of reaching that step is 0

            # check if cache array has a value for this index
            if cache[i] != -1:
                return cache[i] # if it does, return that value -- reusing values to avoid making more function calls

            # save recursive function return values to cache
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            # return value from cache
            return cache[i]

        # return minimum of first & second step values
        return min(dfs(0), dfs(1))


    """
    Regular recursion
    """
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
        
    #     # recursive function
    #     def dfs(i):
    #         # check if input index is equal to or greater than len(cost) -- i.e, the target has been reached
    #         if i >= len(cost):
    #             return 0 # return 0, since the cost of reaching that step is 0
            
    #         # return the addition of current index's cost + min of 1 step & 2 steps
    #         return cost[i] + min(dfs(i + 1), dfs(i + 2))
        
    #     # return minimum of first & second step values
    #     return min(dfs(0), dfs(1))