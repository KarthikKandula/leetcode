class Solution:
    """
    NeetCode Solution (using Set)
        search operations on set is O(1)

    Find the previous value for any given value
        if doesn't exist it could possible be the start of a sequence
        if exists, it's part of a sequence, not start of one

    for start of sequence, keep looping as long as you find the next value
        keep record of current length of sequence
    
    by end should have the longest sequence
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # create a set form input
        longest = 0 # variable to store longest value

        # loop thru input nums
        for n in nums: 
            length = 1 # initialize temp length to 1
            
            # check if prior value is in numset
            if (n-1) in numSet:
                continue # if yes, continue with loop
            
            # loop as long as there is next available value
            while (n+length) in numSet:
                length += 1 # increment length with 1
            
            # replace longest with latest length
            longest = max(length, longest)

        # return value
        return longest

    
    """
    NeetCode Solution (using Set)
        search operations on set is O(1)

    Same as method 1, slightly diff code
    """
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums) # create a set form input
    #     longest = 0 # variable to store longest value

    #     # loop thru input nums
    #     for n in nums: 
    #         length = 1 # initialize temp length to 1
            
    #         # check if prior value is in numset
    #         if (n-1) in numSet:
    #             continue # if yes, continue with loop
            
    #         m = n # temp variable to copy value of n
    #         while (m+1) in numSet: # loop as long as find m+1 in set
    #             length += 1 # increment length (to find sequence)
    #             m += 1 # increment length (to reset for next loop)
            
    #         # find max value for temp length & longest
    #         longest = max(length, longest)

    #     # reutrn value
    #     return longest

    
    """
    Alt Solution
    """
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums)
    #     table = {}
    #     longest = 0

    #     for n in numSet:
    #         x = table.get(n-1, 0)
    #         y = table.get(n+1, 0)

    #         length = x + y + 1

    #         table[n-x] = length
    #         table[n+y] = length

    #         longest = max(length, longest)
    #         # print(f"val {n} \n table {table} \n x {x} y {y}")

    #     return longest
