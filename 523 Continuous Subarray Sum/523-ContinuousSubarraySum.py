class Solution:
    """
    Optimal prefix sum solution

    due to the properties of modulus operator
        it is okay to keep one running remainder 
        as opposed to trying out all sum possibilities 
        then checking if the remainder is 0 at every element
    
    so in plain simple words, we keep adding numbers to remainder & perform modulus operation
        keep track of the modulus values along with indexes
        if a modules value appears again
            it means there was a subarray of sum k that is in between
            so we check for the difference in indexes between current index & prev index
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # cache to store previous mod values
        cache = {0: -1}
        remainder = 0 # running remainder variable

        # loop for input
        for i, n in enumerate(nums):
            # add current number to remainder
            remainder += n
            remainder %= k # modulus with k 

            # check if this remainder is seen before
            if remainder in cache:
                # if seen, check the distance between the indexes, should be atleast 2
                if i - cache[remainder] >= 2:
                    return True
            # if this remainder not seen before
            else:
                # insert into cache
                cache[remainder] = i
        
        # if return isn't hit above, return False
        return False

    """
    Brute Force
    """
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     # if length of input is less than 2
    #     if len(nums) < 2:
    #         return False # return False

    #     # loop for input
    #     for i in range(len(nums)):
    #         # start subarrays from current number
    #         tempSum = nums[i]
    #         # loop fron next index to end
    #         for j in range(i + 1, len(nums)):
    #             # add current num to temp sum
    #             tempSum += nums[j]

    #             # check if modulus is 0
    #             if tempSum % k == 0:
    #                 return True # return True, if condition satisfies

    #     # return False
    #     return False
