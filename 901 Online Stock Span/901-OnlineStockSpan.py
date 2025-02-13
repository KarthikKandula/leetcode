class StockSpanner:

    def __init__(self):
        # stack to implement monotonic decreasing stack
        self.stack = [] # format - (value, index)
        self.counter = 0 # to keep track of the order of values coming in aka the index

    """
    this is a classic monotonic stack problem
        if we look at the problem seriously
            it's a previous greater element problem in disguise
        the twist in this problem is that, we'll have a continuous stream of data coming in
            having to constantly update our stack & derive answers from it
        but to our advantage, we only have to return values that are less than or equal to current values
            this is what monotonic stack implements bloody well
        we remove values from stack that are less than or equal to current value
            once all values are removed, get the top value in stack
                this is the highest value above current price
                get the difference between current index & the higher value index
                it's the answer
    """
    def next(self, price: int) -> int:
        self.counter += 1 # increment counter to account for current value

        # populate stack/update stack -- remove any less values than current price
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop() # pop from stack

        # get the latest index from stack -- this is the prev higher value
        lastIndex = self.stack[-1][1] if self.stack else 0

        # insert current value into stack
        self.stack.append((price, self.counter))

        # return the difference between current counter and the last index
        return self.counter - lastIndex


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)