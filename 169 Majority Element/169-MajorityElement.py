class Solution:
    """
    O(n) time, O(1) space

    to implement the same problem in constant space
        we use the characterists of the problem to our advantage
        since the result is guaranteed to be majority
            we can employ a prefix sum scheme
            increment +1 to majority if current value is same as result we have
            change result if majority ever reaches to 0
                indicates there is a change in frequencies
        by the end of the array, the majority element will end up in result value
    """
    def majorityElement(self, nums: List[int]) -> int:
        # create variables to track maj element & majority count
        res, majority = 0, 0

        # loop for every value in input
        for n in nums:
            # if majority gets to 0, replace with nums
            if majority == 0:
                res = n
            
            # increment/decrement majority value
            majority += 1 if res == n else -1
        
        # return majority element stored in res variable
        return res

    """
    O(n) time, O(n) space

    to find out the majority element in the input array
        create a hashmap, that tracks counts of each value
        keep record of the majority element as we traverse thru the array
        if found an element count greater than current majority, replace with new value
        in the end, return old value
    """
    def majorityElement(self, nums: List[int]) -> int:
        majority = float('-inf') # declare variable for majority
        res = 0 # variable for tracking result

        # create hashmap to store counts
        hashmap = {}

        # loop for every value in nums
        for n in nums:
            # increment count in hashmap for current num
            hashmap[n] = hashmap.get(n, 0) + 1

            # count for current num is greater than majority
            if hashmap[n] > majority:
                majority = hashmap[n] # update majority count to new count
                res = n # replace result value
        
        # return majority element in result
        return res

