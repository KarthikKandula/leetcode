# 151. Reverse Words in a String

1 possible solution for this problem  

### Self Notes


```
Optimal solution
"""
    can solve this using string functions & two pointers
        use split() to get all words in a list
        use two pointers to loop thru the words in opposite directions
            interchange words at i, j location
            decrement both pointers to look at next set of words
        in the end, return a string joining all words with space in btwn
"""

Own solution
"""
    can solve this problem using two pointers
        we need to skip any extra spaces found at the start, end & in between words
            if both pointers are pointing at a space, it's an extra space, ignore it
        we need to get all words
            as soon as both pointers hit anything other than a space, advance only the j pointer until a space is found
        once a space is found, get everything between j & i pointer
            it's a new word, append to result
        reassign both pointers to the position after j space
    
    by the end, reversed string is in result variable
"""
```

