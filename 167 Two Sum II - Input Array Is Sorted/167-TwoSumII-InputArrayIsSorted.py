class Solution:
    """
    Use two pointers, one at start, one at end
        
    compare the sum of start & end 
        if greater than target -> decrease end
        if less than target -> increase start
        if match found -> return indexes
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Initialize left & right pointers
        l, r = 0, len(numbers)-1

        # Loop while left is less than right - not equal to since duplicates not allowed
        while l < r:
            # temp variables to store sum in a loop - increases speed
            temp = numbers[l] + numbers[r]
            # If temp sum & target are same
            if temp == target:
                # return l & r indexes - add 1 as described in question
                return [l+1, r+1]
            # If temp is greater than target - decrease r
            elif temp > target:
                r -= 1
            # If temp is less than target - increase l
            else:
                l += 1

        # No end return needed since a solution is guaranteed
            
