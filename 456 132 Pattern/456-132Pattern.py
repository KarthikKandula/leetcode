class Solution:
    """
    NeetCode Mono Increasing solution

    from the previous implmentation, if we tweak our logic a bit, we get this solution
        the flaw in my implementation is that, it loses track of the values occuring before the lowest value in input
        we adjust for that flaw by also keeping track of the lowest value until a position in the stack
        
        implement a monotonic increasing stack
            by doing this, we maximize the 3 value 
            while minimizing the 1 value
            so in process, we have a larger window to find the 2 value
        keep track of the min value seen before any element 
            insert into stack in format [val, min]
        if at any location, the stack is populated
            and curr num is greater than min value of top element, we've found a solution 
    """
    def find132pattern(self, nums: List[int]) -> bool:
        # stack to implement mono increasing stack
        stack = [] # format - [value, min val]

        # to track min values occuring before a value
        curMin = nums[0]

        # since 0th index could possibly be a 1 value, we can start the loop from 1st index
        for n in nums[1:]:
            # implement increasing stack, remove elements less than current
            while stack and n >= stack[-1][0]:
                stack.pop()
            
            # check if stack is populated and the min value of top element is less than current
            if stack and n > stack[-1][1]:
                # if yes, we've found a solution
                return True
            
            # append current element to stack
            stack.append([n, curMin])
            curMin = min(curMin, n) # update cur min value
        
        # return False if true isn't triggered above
        return False

    """
    My Mono Decreasing solution

    this solution uses a monotonic decreasing stack
        it looks at if a value has been popped in the current iteration
            a popped value means, there is a value greater than current -- possible 3 value
        if the stack is populated -- this is the 1 value
        current value is the 2 value 

        so we've found a solution

    the flaw in this was that if a low value appears mid input, it ignores all possible 1 value appearing before it
    """
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        for i in range(len(nums)):
            pop = False
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
                pop = True
            
            if pop and stack:
                return True
            
            stack.append(i)
        
        return False
