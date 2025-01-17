class Solution:
    """
    this is an XOR operation
        the idea is that since there is only 1 number that appears once
        when XOR is applied to all values in the array where each number occurs twice
        all the twice occuring numbers cancel out & the single one remains
        that's cuz for XOR
            0 ^ 0 = 0
            0 ^ 1 = 1
            1 ^ 1 = 0
        so if we xor same numbers, it'll lead to 0 
            and since numbers appear twice, all those numbers cancel out leaving us with the unique number
    """
    def singleNumber(self, nums: List[int]) -> int:
        # create result variable with 0 since n ^ 0 = n
        res = 0

        # loop thru input nums
        for num in nums:
            # perform xor for each number with result
            res = num ^ res
        
        # return result in the end
        return res
