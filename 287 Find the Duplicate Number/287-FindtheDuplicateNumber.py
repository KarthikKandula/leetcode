class Solution:
    """
    use Floyd's Tortoise & Hare algorithm to solve the problem
        this uses two pointers - slow & fast
            slow -- moves 1 position with each iteration
            fast -- moves 2 positions with each iteration
        the algorithm says these two pointers will meet eventually if there is a cycle within n iterations
            time complexity is O(n)
    
    but this is a bit different since the input is an array
        according to the problem statement there will be n + 1 integers in the array but range is [1, n]
        which means we can consider a linked list of sorts & the integers themselves point to the index of it's value. 
        Also, the input will never spill out
    
    going with this consideration & in accordance with floyd's algorithm
        we take slow & fast pointer
            at the location where these pointers meet, we break the loop
    
        now take another slow pointer -- slow2 starts from beginning
            we move the slow pointer & slow2 pointer one location at a time
                slow pointer stays where it was
            at one particular point, these pointers are going to meet which is the duplicate number
    
    return the duplicate number where slow & slow2 meet
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # create slow & fast pointers -- starting at same location
        slow, fast = 0, 0

        # loop until condition is hit
        while True:
            # move slow pointer by one location
            slow = nums[slow]
            # move fast pointer by two locations
            fast = nums[nums[fast]]

            # if slow & fast meet, break the loop
            if slow == fast:
                break
        
        # create second slow pointer
        slow2 = 0

        # loop until condition is hit
        while True:
            # move slow pointer by one location
            slow = nums[slow]
            # move second slow pointer by one location
            slow2 = nums[slow2]

            # if two slow pointers meet, return slow -- we've found the duplicate
            if slow == slow2:
                return slow # return slow value -- this is the duplicate
