class Solution:
    """
    O(1) space approach

    instead of using stack, we can implement this using constant space
        we need to find the buildings that have a view
        i.e., all the buildings that don't have a higher building after it
        if we traverse the array in reverse order
            only max values & values that beat this max value has a view
            we can eliminate the array & use a single variable to record the max value 
            if a higher value is found, insert that value into the result array
    """
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []

        maxHeight = -1

        for i in range(len(heights) - 1, -1, -1):
            if maxHeight < heights[i]:
                res.append(i)

                maxHeight = heights[i]
        
        res.reverse()

        return res

    """
    Monotonic Stack approach

    this is similar to any monotonic stack
        looking carefully at the problem we realize this is a monotonic increasing stack problem
        but in the end, we return values in the stack
    """
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            
            stack.append(i)

        return stack
