class Solution:
    """
    Use two pointers to solve the problem

    Loop thru the input array by checking the current capacity for that loop
        current capacity is min of current heights * the distance between those heights
        replace output maxCap is current capacity is higher
    
    Keep pointers moving based on the lowest value
        additional condition to move left is values are equal
    """
    def maxArea(self, height: List[int]) -> int:
        # left, right pointers
        l, r = 0, len(height) - 1
        maxCap = 0 # variable to store max capacity

        # loop as long as left < right
        while l < r:
            # Calculate capacity for current iteration - min of current heights * distance between pointers
            currentCap = min(height[l], height[r]) * (r - l)

            # assign highest value to output variable
            maxCap = max(maxCap, currentCap)

            # Increment left pointer if height[l] < height[r] - to keep checking for other values
            if height[l] <= height[r]:
                l += 1 # Increment
            elif height[l] > height[r]: # Decrement right pointer if height[l] > height[r]
                r -= 1 # Decrement

        # Return max capacity 
        return maxCap 

