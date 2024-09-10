# 49. Group Anagrams

1 possible solution for this problem

## Method 1

Use a hashmap (w/ defaultdict(list)) to record no. of times each value occurs  
Use count (26 indexes for each letter) to record the occurences of each value in strs, add count to hashmap  
Do the same for each value & append if found the same value in hashmap  

```
    """
    NeetCode solution

        Use hashmap to keep a record of all values in input strs
            Use count (26 indexes for each letter from a to z) to record occurences for each value in strs
            add count to res & append the strs value if match

        return hashmap's values as result set 
"""
```

## Method 2 (My Solution)

Use a hashmap to record no. of times each value occurs  
Use count (as a dict) to record how many times each value occurs in each value of strs  
But can't use this count hashmap since it's not hashable in a hashmap/dict, hence this won't work 
