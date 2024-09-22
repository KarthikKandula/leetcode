class MinStack:
    # Initalize object
    def __init__(self):
        self.stack = [] # Create stack
        self.minStack = [] # Create stack to store minimum values

    # push into stack at the end
    def push(self, val: int) -> None:
        # append into stack
        self.stack.append(val)
        
        # getMin operation
        if self.minStack: # If minStack has any values
            # Compare if input val is less than last minStack val
            if val <= self.minStack[-1]:
                # Append to minStack if yes
                self.minStack.append(val)
        else: # if minStack doesn't have any values
            self.minStack.append(val) # Append to minStack - usually to cover first variable

    # pop from stack - from the end
    def pop(self) -> None:
        # pop from stack & store in v
        v = self.stack.pop()
        
        # Compare if v == last minStack value
        if self.minStack[-1] == v:
            self.minStack.pop() # pop if true, to update the minimum value

    # get top element of the stack
    def top(self) -> int:
        return self.stack[-1] # get last element from stack

    # Retrieve min element in the stack
    def getMin(self) -> int:
        return self.minStack[-1] # get last element from minStack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()