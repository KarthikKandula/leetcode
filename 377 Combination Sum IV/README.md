# 377. Combination Sum IV

1 possible solution for this problem  


```
"""
    this is a bottom up solution focusing on finding permutations
        instead of finding the no. of ways from the top, we find the no. of ways from bottom to top
        we try to find how many ways there are to find every sum between 1 -> target
        using the previous computed sums, we find next numbers

    create a cache to track the no. of times a sum can be formed
        initialize 0 --> 1 since there is exactly 1 way to form the sum 0, but using no elements
        now loop for each possible total value until target
        loop thru each number in input 
            add the no. of times this total can be formed by adding the number from nums i.e total - n
            add the no. of times to this total to the cache
        do this until target & we have the no. of combinations in the cache
"""
```

