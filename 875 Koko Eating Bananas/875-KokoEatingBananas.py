class Solution:
    """
    Use binary search to solve the problem
        the problem asks us to find the lowest possible value that satisfies a condition
        there are a range of values the answer can be in, to efficiently narrow down the possible values, we can use binary search

    take two pointers - left & right, on opposite ends of the range of possible values
        possible values are from 1....max(piles)
            anything less than 1 doesn't make sense & anything more than piles would be too fast
        
    loop while left pointer <= right pointer (since l & r can be at the same value & that can be the answer)
        calculate mid point for this iteration
        calculate hours taken to finish the pile
        if hours <= h (hours guards are away)
            it satisfies the condition, could be a possible answer
            decrement the right pointer since any other possible values are in the left subarray
        else
            it means it's going to take more speed to finish all the piles
            increment the left pointer, since any possible values are in right subarray
    
    loop thru end & answer is in result variable
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left & right pointers - either side of the possible range of values
        l, r = 1, max(piles)
        res = r # result value, initialize with the max possible value, since we need the lowest, any value found is easily replacable

        # loop while left is less than or equal to r
        while l <= r:
            k = (l + r) // 2 # find mid point in the current range

            hours = 0 # variable to track hours taken for this particular iteration

            # loop thru the input array
            for p in piles:
                hours += math.ceil(p / k) # calculate the number of hours taken to eat each pile - round up acc to problem

            # after hours are calculated, compare with the hours guards are done
            # if hours <= h, we found a possible solution
            if hours <= h:
                res = min(k, res) # update result variable with the lowest value
                r = k - 1 # decrement right pointer, since any future possible value exists in left subarray
            else:
                l = k + 1 # increment left pointer, since any future possible value exists in right subarray

        # return result variable
        return res
