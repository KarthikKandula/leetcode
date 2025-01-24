class MyQueue:

    def __init__(self):
        # create two stacks
        self.stack1 = [] # for inserting data in
        self.stack2 = [] # for representing data in queue format -- after transfer

    def push(self, x: int) -> None:
        # insert elements into first stack
        self.stack1.append(x)

    def pop(self) -> int:
        # if s2 is empty --> push values into s2
        if not self.stack2:
            # loop for all values in stack 1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # pop from top of s2
        return self.stack2.pop()

    def peek(self) -> int:
        # if s2 is empty --> push values into s2
        if not self.stack2:
            # loop for all values in stack 1
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # peek from top of s2
        return self.stack2[-1]        

    def empty(self) -> bool:
        # return False is both stacks are empty else True
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()