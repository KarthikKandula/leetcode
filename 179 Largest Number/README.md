# 179. Largest Number

1 possible solution for this problem  

### Self Notes


```
"""
    Found solution

    use sort() to sort nums as strings in descending order (reverse=True).
        The key function for sorting is lambda x: x*10.
            the idea is to "extend" the string by repeating it 10 times, ensures the correct order during sorting
            Since max possible digit length of numbers in nums is 10 (as per constraints)
            repeating string 10 times ensures all possible concatenation orders are correctly represented
"""

"""
    NeetCode solution

    custom comparator (compare) determines the order in which two numbers should appear to form the largest possible number
        comparison is based on string concatenation
            If n1 + n2 is greater than n2 + n1 --> n1 should come before n2.
                Otherwise, n2 should come before n1.
    
    Why n1 + n2 > n2 + n1?
        This checks the concatenated result of placing n1 before n2 versus placing n2 before n1
        By choosing the order that produces the larger concatenated result, we ensure the largest possible number is formed
        
        Returning -1 or 1:
        In Python's sorted(), a comparator must return
            -1 if the first element is smaller,
            1 if the second element is smaller.
            Returning -1 ensures that n1 comes before n2 in the sorted list.
"""
```

