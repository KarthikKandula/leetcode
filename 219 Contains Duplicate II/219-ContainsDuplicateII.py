class Solution:
    """
    O(k) solution

    we can solve this problem in better space using hashset of size k
        keep dynamically removing elements that are behind k places in the input
        using this we can check if the value is in the set easily
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set() # of size k, dynamically managed

        # loop thru input
        for i, n in enumerate(nums):
            # if i is greater than k, we can start removing elements from set
            if i > k:
                # remove values behind k indices form set
                seen.remove(nums[i - k - 1])
            
            # if number is in seen, return True
            if n in seen:
                return True
            
            # add current number to set
            seen.add(n)

        # return False, if return inside isn't triggered
        return False

    """
    O(n) solution

    use a hashmap to keep track of values seen before
        when a value is in hashmap
        check the difference of the index with current index
        if it's less than or equal to k, return True
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create hashmap
        hashmap = {}

        # loop thru input
        for i, n in enumerate(nums):
            # if current number is in hashmap
            if n in hashmap:
                # check if the differnce in indexes is within limits
                if abs(hashmap[n] - i) <= k:
                    return True # return True, if yes
            
            # insert into hashmap, if already appearing, updating the index value to most recently seen
            hashmap[n] = i
        
        # return false, if return inside isn't triggered
        return False
