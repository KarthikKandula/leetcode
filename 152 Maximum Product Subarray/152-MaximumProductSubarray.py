class Solution:
    """
    this is a traditional dp problem
        a major issue appears with -ve numbers since it keeps fluctuating b/w +ve & -ve with each multiplication
        to get around this issue, we keep track of max product until now & min product until now
        keep updating this value as we keep moving along in the array
        so essentially, we're keeping track of both min & max values since with -ve values they can swing in any direction
    
    create a result variable, assign max value from the input
    create two variables, assign both to 0
        curMax -- tracks the max value 
        curMin -- track the min value 

    loop thru the input
        if any number is 0, assign curMax, curMin to 1
            making them neutral & cutting off product values from before
        assign curMax to temp variable 
            to use in calculating curMin so as to not use newly calculated curMax
        cacluate new curMax for this number
            take the max of current number multiplies by curMax, curMin & itself alone
        cacluate new curMin for this number
            take the min of current number multiplies by curMax, curMin & itself alone
        get max value for result variable
    
    in the end, return result variable
    """
    def maxProduct(self, nums: List[int]) -> int:
        
        # assign max value to result variable
        res = max(nums)

        # assign current max & current min to neutral values 
        curMax, curMin = 1, 1

        # loop thru input nums
        for n in nums:
            # check if current no. is 0, we'll make the values neutral
            if n == 0:
                curMax, curMin = 1, 1
                continue
            
            # save curMax value in a temp variable
            temp = curMax # to use previous curMax value in calculating curMin
            curMax = max(n * curMax, n * curMin, n) # get the max value of n * to curMax & curMin -- to handle negative no's
            curMin = min(n * temp, n * curMin, n) # get the min value of n * to curMax & curMin -- to handle negative no's

            # print(f"n {n}, curMax {curMax}, curMin {curMin}, res {res}")

            # get max value of res & curMax
            res = max(res, curMax)
        
        # return result
        return res

        # def dfs(i):
        #     if i >= len(nums):
        #         return 1
            
        #     res = dfs(i + 1)
        #     if res == nums[i]:
        #         return nums[i]
        #     else:
        #         return max(nums[i], nums[i] * res)
        
        # return dfs(0)