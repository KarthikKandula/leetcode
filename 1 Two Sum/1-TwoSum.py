class Solution:
    """
    Optimized O(n) solution using hashmap/table

    add the diff to target for each element to hashmap
    if current element found in hashmap, return indices
        else add diff to hashmap & continue to end
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        # Declare hashmap to store processed elements
        hashmap = {}

        # Loop thru input array nums
        for i in range(len(nums)):
            # Check if current value exists in hashmap
            if nums[i] in hashmap:
                # return indices if exists
                return [i, hashmap[nums[i]]]
            else: # if current value doesn't exist in hashmap
                # calculate diff for the current val
                diff = target - nums[i]
                hashmap[diff] = i # add current val & index to hashmap

    """
    Optimized O(n) solution using hashmap/table

    add each element to a hashmap, find the diff to target
    if diff exists in hashmap, return indices
    """
    # def twoSum(self, nums: List[int], target: int) -> List[int]: 
    #     # Declare hashmap to store processed elements
    #     hashmap = {}

    #     # Loop to go through enumerated nums
    #     for i, n in enumerate(nums):
    #         # Find difference between target & current number n
    #         diff = target - n

    #         # Check if difference exists in hashmap - if diff exists return current indices
    #         if diff in hashmap:
    #             return [hashmap[diff], i]
            
    #         # Add current number n & index i to hashmap
    #         hashmap[n] = i


    """
    Brute Force solution

    Take each element, add it with rest of elements
    If reached target, return indices
    """
    # def twoSum(self, nums: List[int], target: int) -> List[int]: 
    #     for c1, x in enumerate(nums):
    #         for c2 in range(c1+1,len(nums)): # nums:
    #             if x + nums[c2] == target:
    #                 return ([c1, c2])
