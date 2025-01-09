# 169. Majority Element

1 possible solution for this problem  


```
"""
    O(n) time, O(1) space

    to implement the same problem in constant space
        we use the characterists of the problem to our advantage
        since the result is guaranteed to be majority
            we can employ a prefix sum scheme
            increment +1 to majority if current value is same as result we have
            change result if majority ever reaches to 0
                indicates there is a change in frequencies
        by the end of the array, the majority element will end up in result value
"""

"""
    O(n) time, O(n) space

    to find out the majority element in the input array
        create a hashmap, that tracks counts of each value
        keep record of the majority element as we traverse thru the array
        if found an element count greater than current majority, replace with new value
        in the end, return old value
"""
```

