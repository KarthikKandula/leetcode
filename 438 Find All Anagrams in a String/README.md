# 438. Find All Anagrams in a String

1 possible solution for this problem  


```
"""
    we can solve the problem using sliding window & frequency hashmaps
        the twist with this problem is that
            we need to decrement left pointer for each iteration, to maintain constant window length
            update left pointer frequency in hashmap

            if at any point the frequencies match, add that index to result array
        return result array in end
"""
```

