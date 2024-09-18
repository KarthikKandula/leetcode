# 121. Best Time to Buy and Sell Stock

1 possible solution for this problem

## Method 1

The problem statement asks us to go thru the input array & find the lowest possible point to buy & highest possible point to sell.  
To achieve this we can use the two pointer sliding window method, assign two pointers next to each other at start & go thru the entire input check for lowest values, replacing sell & buy pointers accordingly.  

```
"""
    Use two pointer sliding window method to solve the problem
        doing this we get to compare each variable with each other

    Use two pointers - buy & sell assigned to 0th & 1st index respectively
        so we get to go thru the entire input in a sliding window method
    
    Loop thru input as long as sell < length of input
        calculate profit & replace maxProfit along the way
        check if sell price is less than buy price
            if yes, we have found a new low price to buy
        increment sell in each iteration to compare next price
"""
```
