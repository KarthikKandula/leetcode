class Solution:
    """
    to solve this problem we use Prefix Sum with Hashmap
        one way to find a subarray is to use the formula - sum(nums[i:j]) = prefix[j] - prefix[i-1]
        we use this forumla to max
        calculate prefix sum until each location
            and insert it into the hashmap
        check the diff to k for each location
            if we've seen this diff value before until now
            if we've seen it, means we can remove that subarray from the current subarray & sum equals k
            we can be sure it forms a valid subarray cuz, all calculations now start from 0
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 # store result
        prefix = 0 # to calculate prefix
        hashmap = {0: 1} # initialize hashmap to 0 --> to handle cases where we get exact match with k

        # loop for each value in input
        for num in nums:
            prefix += num # add current value to prefix

            diff = prefix - k # get difference to k

            # check if we've seen the diff value before in hashmap
            if diff in hashmap:
                # if we have, we can remove that particular subarray from the current one & we get a target subarray
                res += hashmap[diff] # append how many occurences of diff to result

            # add this prefix to hashmap -- to handle if this is the diff in future
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        
        # return result val
        return res

    """
    same implemention with different code
    """
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0 # store result
    #     prefix = 0 # to calculate prefix 
    #     hashmap = defaultdict(int) # initialize hashmap to with defdict int

    #     # loop for each value in input
    #     for num in nums:
    #         prefix += num # add current value to prefix

    #         # if we find an exact match to prefix, add 1 to result
    #         if prefix == k:
    #             res += 1

    #         diff = prefix - k # get difference to k

    #         # check if we've seen the diff value before in hashmap
    #         if diff in hashmap:
    #             res += hashmap[diff]
            
    #         # add this prefix to hashmap -- to handle if this is the diff in future
    #         hashmap[prefix] += 1

    #     # return result val
    #     return res
