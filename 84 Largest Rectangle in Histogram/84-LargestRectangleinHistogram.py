class Solution:
    """
    use stack to solve the problem
        trick is to store values in pairs in stack - (index, height)

    loop thru the input
        check if there are any values in the stack that are greater than current height
            if there are, pop them all out since they can't be extended forward to current height, they have been broken
                get the max area of the popped value & replace if max
                since the popped value is greater than current, it means current height can be extended back, so we take the index of that variable 
        append current height to stack with
            our own index if there are no values higher in stack
            if we popped any values out, we use that index value, there is a variable for this
    
    after looping thru all the values, there might still be values in the stack
        to find if there is a possibility of max area in those, 
        loop thru the stack 
            find max area for each value in stack - use formula (height * (length of input - index))
            replace if max
    
    loop to the end & maxArea variable will have max value
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack to keep track of index & heights
        stack = [] # push into stack in pairs (index, height)
        maxArea = 0 # variable to store maxArea

        # loop thru input heights
        for i, h in enumerate(heights):
            start = i # assign the current index to a temp variable start

            # loop stack to see if there are any heights that are greater than current height, if exists, they can't be continued, pop em out
            while stack and stack[-1][1] > h:
                # pop from stack & store in variables
                tempIndex, tempHeight = stack.pop()
                # tempMaxArea = tempHeight * (i - tempIndex) # calculate maxArea for the popped out height
                maxArea = max(maxArea, tempHeight * (i - tempIndex)) # get maxArea

                start = tempIndex # assign popped index to start, since current height is extendable to that height
            
            # append (index, height) to stack
            stack.append([start, h])

        # there will be values left out in stack, to calculate max area for those values
        # loop thru stack
        for i, h in stack:
            # calculate maxArea for current location
            # tempMaxArea = h * (len(heights) - i)

            # get maxArea
            maxArea = max(maxArea, h * (len(heights) - i))

        # return max area
        return maxArea
