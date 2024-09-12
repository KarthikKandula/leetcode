# 128. Longest Consecutive Sequence

2 possible solutions for this problem
* 2 solutions are same version w/ diff code

## Method 1

Use set to solve the problem, search operations of set is O(1)  
A sequence is nothing but consecutive numbers, which means the start wouldn't have a value before it. Our target is to find this value & keep looking for the next value. keep looping until you keep finding next values, once stopped update the longest sequence value & continue till the end.

```
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
```

### Method 1a

Same solution as Method 1 but slightly different code

## Method 2

Solution found in solution section. a bit complex
