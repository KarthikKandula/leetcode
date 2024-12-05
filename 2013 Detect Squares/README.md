# 2013. Detect Squares

1 possible solution for this problem  

### Self Notes


```
"""
    the idea is to perform basic multiplication but convert it to code
        while performing multiplication for 2 digit or more digit numbers
        we do it in a nested loop formate i.e, multiply each digit with each other
        and after each levels do it so as to skip one level from right

        we achieve the same functionality but by using nested loops
        the functionaly of skipping levels from right can be achieved by adding both indexes
    
    create a result array with max possible length 
        i.e add length of both numbers
    
    reverse both inputs since we'll be processing both values in reverse
    
    create a nested loop to go thru each element for both numbers
        multiply each location values
        insert the product to the result array in [i + j] location -- skipping levels from right
            value to keep in the location is remainder -- %
        if any carry exists, insert in next location [i + j + 1]
            carry is the product of the number -- //
    
    after nested loop is done product is in reverse order in result array
        reverse the array again 
        remove any preceding 0's
    
    convert values to string & generate string to return output
"""
```

