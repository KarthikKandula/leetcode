# 242. Valid Anagram

3 possible solutions for this problem

## Method 1

Use 1 hashmap to record no. of times each value occurs & deduct values from same hashmap going thru the second input  

```
"""
    solution using hashmaps
        one hashmap

        loop thru s & add the count of each value into the hashmap 
        loop thru t & subtract the count of each value into the hashmap 

        if any value in hashmapS not equal to 0
            return false
        else
            return true
"""
```

## Method 2

Use 2 hashmaps to record no. of times each value occurs in each input & compare values at the end. If mismatch return false, else true 

```
"""
    solution using hashmaps
        two hashmaps
            each for s & t

        loop thru s & add the count of each value into s hashmap 
        loop thru t & add the count of each value into t hashmap 

        compare values in hashmapS & hashmapT
            if any value don't match
                return false
            else
                return true
"""
```


## Method 3

Without using hashmaps, use list func to convert string to array of chars & remove each value as occured in 2nd input, if any value not in charList -> return 0  
Compare length of list at the end, if 0, true else false

```
"""
    My solution

    get list of all chars in s using list func
        loop thru t & remove each value
        if any value not in charList (from t) -> return false

        at the end compare if length of charList is 0
            if length is 0
                return true
            else
                return false
"""
```
