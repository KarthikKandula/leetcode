class Solution:
    """
    If you divide the problems into sub-problems, it's similar to two sum II

    A sorted array helps to solve easily
    Use two pointers inside an outer loop that iterates thru numbers in a order
        introduce code to handle for duplicates
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort input array to make it easy for solution

        res = [] # array to record result

        # loop for every number in input nums
        for i, v in enumerate(nums):
            # check if a number is same as the number before it, since array is sorted & we don't want duplicate sets
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip that value

            # create left & right pointers
            l, r = i + 1, len(nums) - 1
            while l < r: # loop while left < right
                temp = v + nums[l] + nums[r] # temp variable to store sum of three current values

                # if sum is greater than zero, decrement right pointer -> similar to two sum II 
                if temp > 0:
                    r -= 1 # decrement right pointer
                # if sum is less than zero, increment left pointer -> similar to two sum II 
                elif temp < 0:
                    l += 1 # increment left pointer
                else: # loop reaches here if sum == 0
                    # append three current values to result array
                    res.append([v, nums[l], nums[r]])
                    
                    # increment left & decrement right pointers, since we don't want duplicates
                    l += 1
                    r -= 1

                    # after incrementing check if values are similar, to eliminate duplicates
                    while nums[l] == nums[l-1] and l < r: # using while loop to handle muliple duplicate values
                        l += 1 # increment again

        # return result set
        return res
