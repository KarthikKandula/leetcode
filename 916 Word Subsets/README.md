# 916. Word Subsets

1 possible solution for this problem  


```
"""
    this problem can be solved using frequency hashmap/array
        the only catch being, we need to calculate frequency counters for each word
        a slight twist would be to compress all words in words2 to a single max word
            aka if requirements are 'o', 'oo', then we'd only need 'oo' since 'o' is automatically satisfied
        once we generate the freq array via ascii values
        match these values against each value in words1
            only if all conditions are satisfied
            add to output array
        return output array
"""
```

