class Solution:
    """
    Use two pointers to solve the problem
    
    """
    def trap(self, height: List[int]) -> int:
        # Create left & right pointers on opposite ends of input height
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r] # Create maxL & maxR values to track max values to left & right of any index
        res = 0 # variable to store result
        
        # loop while left < right
        while l < r:
            # check if maxL <= maxR to increment respective pointers
            if maxL <= maxR:
                l += 1 # increment left pointer, incrementing first since the first position can't store any water
                maxL = max(maxL, height[l]) # get maxL value between current maxL & current left pointer value in input height
                res += abs(maxL - height[l]) # calculate the current water holding capacity & add to result variable
                # res += abs(min(maxL, maxR) - height[l])
            else: # maxR is less than maxL, enter to increment respective pointers
                r -= 1 # decrement right pointer, decrementing since the last position can't store any water
                maxR = max(maxR, height[r]) # get maxR value between current maxR & current right pointer value in input height
                res += abs(maxR - height[r]) # calculate the current water holding capacity & add to result variable
                # res += abs(min(maxL, maxR) - height[r])

        # return result variable
        return res

