# 238. Product of Array Except Self

1 possible solution for this problem

## Method 1

The product of all other elements of array except self is the product of
* prefix (elements before it)
* postfix (elements after it)

If we multiply these products of prefix & postfix we get the desired answer  

To achieve this we use an array to keep track of prefix & postfix for corresponding position.

```
"""
    Create output array & assign it with 1 for length of nums

    Use a process as prefix sum
        the product of all other elements other than current elements is basically the 
            product of prefixes (elements before it) multiplied by the product of postfixes (elements after it) 
        For this we use two variables to keep track of pre & post products

    prefixes
        assign the prefix value in the current index
        multiply the current nums value with prefix (to use in next index)

    postfixes
        slight modification in logic
        multiply the postfix to current output array index
        multiply the postfix to current nums index (to use in next index)
    
    by the end of postfix loop, output array would have desired values
"""
```

same solution in just different code is as below  
```
"""
    Create output array & use it throught the process to get required result

    First - save the product of prefixes of each element from nums in output
        Do this start -> end
        Initialize pre to 1
        Multiply output element in current index with pre
        Multiply pre with current nums index - to update next element

    Second - multiply product of post fixes to elements in output - it already has prefixes
        Do this end -> start
        Initialize post to 1
        Multiply output element in current index with post
        Multiply post with current nums index - to update next element
        Decrease index by 1
"""
```
