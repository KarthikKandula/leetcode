class Solution:
    """
    This is a classic binary search problem
        if we look at the problem statement a bit
            we realize that there exists a min capacity, i.e the max value in the array
            so if there exists a max value, it is a binary search problem
                the max value is the sum of all weights in the input
        if we loop between the min & max value 
            check for a right fit, the least value that satisfies this condition is the answer
        to see if we can satisfy for a certain capacity value
            go in order & add to a temp value
                if at any time, the temp value is greater than capacity
                    reset capacity value
                    increment days needed value
                done until end, we'll know how many days this capacity needs
        the lowest capacity at which all weights can be carried is the answer
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # create left & right pointers
        l, r = max(weights), sum(weights)
        # variable to store result
        res = r

        # loop while left & right don't meet 
        while l < r:
            # get mid value
            m = (l + r) // 2

            # calculate if all packages can be shipped with this mid value
            daysNeeded, curWeight = 1, 0

            # loop for each weight in input
            for w in weights:
                # if weight is above mid at any point, reset
                if curWeight + w > m:
                    daysNeeded += 1 # increment days needed
                    curWeight = 0 # reset weight to 0
                
                # append w to current weight calc
                curWeight += w
            
            # after loop is done, if more days are needed, answer is in right hand side
            if daysNeeded > days:
                # reassign left to after mid, to search in right hand side
                l = m + 1
            # days needed is less than or equal to days, which means, result is present here
            else:
                # days needed is less than available days, get the min value
                res = min(res, m)
                r = m # reassign right pointer to mid to search for an even lower value
        
        # return result value
        return res
