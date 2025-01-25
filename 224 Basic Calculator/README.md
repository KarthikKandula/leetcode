# 224. Basic Calculator

1 possible solution for this problem  


```
"""
    this implementation of basic calculator uses stack & some twists & turns
        the idea is to compute the value continuosly
        we need 3 variables to calculate the result efficiently
            res -- to store the running result
                as well as to seperate out the calcs for inside paranthesis ops
            num -- to store the current running number
                is reset when a possibility of new number exists
                aka a new sign/paranthesis
            sign -- to store the next numbers sign
    
    loop thru each value in the input string
        if current is digit
            add to num -- handle for multiple digits
        if current is a sign
            num has ended
                add this num to result with sign
            update sign for next number
            reset num -- for next number
        if current is a open paranthesis
            there are new possiblities, new calcs to be done
                we require fresh num, sign & res
            insert current res & sign into stack 
                storing them off -- will retreive when closing paranthesis
            reset res & sign -- for in paran ops
        if current is a closing paranthesis
            we need to calculate current paran values with prev values
            finish processing current num -- add to result
                will be the final in paran value
            get the sign, prev res from stack
            update res with prev values -- will be the overall result going forward
            reset num
        while returning, it's possible last value is a num
            so we perform one final adjusting to result before returning
"""
```

