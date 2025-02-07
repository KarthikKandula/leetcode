# 122. Best Time to Buy and Sell Stock II

1 possible solution for this problem  


```
"""
    this is a simple clean strategy
        that just relies on the changes in price on a daily basis
        since we can do infinite amount of transactions but can only hold one stock at a time
        we only need to compare with the previous day's value & settle those immediately
        once we add all the consecutive difference values, we get the final value
"""

"""
    use dp techniques to calculate the differences between each day's values
        we can do two possible operations
            skip that day -- we can choose not to buy or sell this day, possibility of higher price next day
            buy/sell -- do opposite of whatever operation was performed before
        by implementing these two operations, we get the max profit possible 
        by using a flag to indicate if bought/sold, we can accomodate multiple transactions for the input
"""
```

