class Solution:
    """
    use monotonic stack (decreasing) and reverse order comparision to solve the problem
        the problem required to find the max value of j - i satisfying a condition
        a decreasing monotonic stack is best suited for this kind of problems
        first we populate the monotonic stack from start in decreasing order
        then loop from the end to compare value form the stack as well as value from end
            if satisfied the condition nums[i] <= nums[j]
            get the diff value & update a variable
        once all the values have been visited, we get the max possible value in result variable
    """
    def maxWidthRamp(self, nums: List[int]) -> int:
        # stack to implement monotonic stack
        stack = []

        # loop for length of input
        for i in range(len(nums)):
            # building decreasing monotonic stack
            # if stack isn't initialized or current value is less than last value in stack
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i) # add to stack

        # to record final result
        ramp = 0

        # loop for length of input in reverse order
        for j in range(len(nums) -1, -1, -1):

            # loop while stack is initialized and value in stack is less than current j value
            while stack and nums[stack[-1]] <= nums[j]:
                ramp = max(ramp, j - stack[-1]) # get max value from diff
                stack.pop() # remove from stack, extracted max possible value from this index
        
        # return final value
        return ramp
