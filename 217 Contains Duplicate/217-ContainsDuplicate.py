class Solution:
    """
    Use set
        Set returns unique values for an input

    if length of input != length of set, return True, else False
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set for input nums
        s = set(nums)

        print(s)

        # Return True if length of set != length of input nums, else False
        return True if len(s) != len(nums) else False


    """ -->'Time Limit Exceeded'<--
        Create an array to take note of unique values in nums
        for each value in nums
            if value already exists in unique -> duplicate value, return True
            if doesn't exist -> append to unique

        if full nums in traversed -> it means values are unique
    """
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     # Get unique values from nums
    #     unique = []
    #     for i in nums:
    #         if i in unique:
    #             return True
    #         else:
    #             unique.append(i)

    #     # print(unique)
    
    #     return False


    """
    Sorting & compare two adjacent elements 
    """
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     # Sort input nums in asc order
    #     nums.sort()

    #     # Loop through input nums - len - 1 since comparing the the next element in each comparision
    #     for i in range(len(nums)-1):
    #         # Compare current num to next element 
    #         if nums[i] == nums[i+1]:
    #             # If match, return True
    #             return True
        
    #     # If program reachess to this position, it means no duplicates exist
    #     return False