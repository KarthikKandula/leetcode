# 383. Ransom Note

2 possible solution for this problem  


```
"""
    One Hashmaps approach
        get the count of each char from magazine
        now, go thru each char in ransomNote 
            decrement each char as seen from magazine hashmap
            if any letter is 0 before decrementing
            it means, there are not enough letters in magazine
                return False
        if false condition isn't hit inside, return True
"""

"""
    Two Hashmaps approach
        get counts of two inputs
        now go thru the chars & counts from ransom note
            check if the count from magazine matches or exceeds the value
            if it doesn't, return False
        if false condition isn't hit, return True
"""
```

