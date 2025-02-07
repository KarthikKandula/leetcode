class Solution:
    """
    we can approach the problem as having to build buildings adjacent to each other
        consider it so that, if we build a building of size 3, we've already build the build of size 2 & 1 as well
        but if we need to build another building of size 5 beside a 1, since 1 is already existing
            we'd only need to build for size 4, so add 4 to the final value
        this value when a value is higher than it's prev value, we need to build it up
        after doing this for entire array, we have the final value in result
    """
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0 # variable to track the no. of operations required -- global value
        prevVal = 0 # variable to track the previous value

        # loop for length of input
        for i in range(len(target)):
            # if previous value is less than current value, we need to build something up
            if prevVal < target[i]:
                # add the difference to global value
                operations += (target[i] - prevVal)
            
            # assign current value to prev value
            prevVal = target[i]

        # return final value
        return operations
