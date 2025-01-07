# 560. Subarray Sum Equals K

1 possible solution for this problem  


```
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
```

