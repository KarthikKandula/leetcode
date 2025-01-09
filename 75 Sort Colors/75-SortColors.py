class Solution:
    """
    to do the same operation with using extra space
        since there are only two colors, we use that to our advantage
        we track the first & last color using pointers at either end
        if we encounter the first color
            place in in first pointer location & increment the pointer
        if we encounter the last color
            place in in last pointer location & decrement the pointer
            while doing this, we also handle an edge case
                incase the value being replaced is a 0 or 1, we need to process it again
                so we decrement i pointer to keep it in the same place
        by the end, colors will be sorted        
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create variables for tracking red & blue colors on opposite sides
        r, b = 0, len(nums) - 1

        # initialize pointer i
        i = 0

        # loop while i is less than blue pointer
        while i <= b:
            # if current color is 0 aka red
            if nums[i] == 0:
                # replace with red pointer location
                nums[i], nums[r] = nums[r], nums[i]

                # increment red pointer
                r += 1
            # if current color is 0 aka blue
            elif nums[i] == 2:
                # replace with blue pointer location
                nums[i], nums[b] = nums[b], nums[i]

                # decrement blue pointer
                b -= 1

                # decrement i pointer -- to handle case where replaced value is 0 or 1, to process it again
                i -= 1
            
            # increment i pointer
            i += 1

    """
    use a hashmap to count number of occurrences of each value
        loop thru input array
            check the count of a particular color 
                if it is not 0, place that color in the location 
                repeat for each color, until their counts are exhausted
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create a hashmap with counters
        hashmap = Counter(nums)

        # loop thru input array
        for i in range(len(nums)):
            # check count for red
            while hashmap[0] != 0:
                # if it still has count, replace current location with 0
                nums[i] = 0

                # decrement count in hashmap
                hashmap[0] -= 1
                i += 1 # increment i count
            
            # check count for white
            while hashmap[1] != 0:
                # if it still has count, replace current location with 1
                nums[i] = 1

                # decrement count in hashmap
                hashmap[1] -= 1
                i += 1 # increment i count
            
            # check count for blue
            while hashmap[2] != 0:
                # if it still has count, replace current location with 2
                nums[i] = 2

                # decrement count in hashmap
                hashmap[2] -= 1
                i += 1 # increment i count

