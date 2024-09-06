# 1. Two Sum

3 possible solutions for this problem  
2 solutions are identical, slight change in approach

## Method 1

Use hashmap to record the difference for an index, try to find the corresponding value in hashmap, if exists, return indices, continue doing so until a solution is found

```
"""
    Optimized O(n) solution using hashmap/table

    add the diff to target for each element to hashmap
    if current element found in hashmap, return indices
        else add diff to hashmap & continue to end
"""
```

## Method 2

Use hashmap to record the value at an index, try to find the difference to the corresponding value in hashmap, if exists, return indices, continue doing so until a solution is found

```
    """
    Optimized O(n) solution using hashmap/table

    add each element to a hashmap, find the diff to target
    if diff exists in hashmap, return indices
"""
```


## Method 3

Your regular brute force using two for loops, comaring each value with the other

```
"""
    Brute Force solution -- My solution

    Take each element, add it with rest of elements
    If reached target, return indices
"""
```
