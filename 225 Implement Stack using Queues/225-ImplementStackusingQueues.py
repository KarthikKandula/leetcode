class MyStack:
    """
    1 Queue flow
    """

    def __init__(self):
        # queue 1 to record all values
        self.q = deque()

    def push(self, x: int) -> None:
        # add input value to q1
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        print(self.q)

    def pop(self) -> int:
        # return popVal
        return self.q.popleft()

    def top(self) -> int:
        # return topVal
        return self.q[0]

    def empty(self) -> bool:
        # return if length of q1 is 0
        return len(self.q) == 0

class MyStack:
    """
    2 Queue flow
    """

    def __init__(self):
        # queue 1 to record all values
        self.q1 = deque()
        # queue 2 for pop & top ops
        self.q2 = deque()

    def push(self, x: int) -> None:
        # add input value to q1
        self.q1.append(x)

    def pop(self) -> int:
        # loop thru q1 until 1 element is left
        while len(self.q1) > 1:
            # append popped element to q2
            self.q2.append(self.q1.popleft())
        
        # pop last value from q1
        popVal = self.q1.popleft()
        # swap values in q1 & q2
        self.q1, self.q2 = self.q2, self.q1

        # return popVal
        return popVal

    def top(self) -> int:
        # loop thru q1 until 1 element is left
        while len(self.q1) > 1:
            # append popped element to q2
            self.q2.append(self.q1.popleft())
        
        # get last value from q1
        topVal = self.q1[0]
        self.q2.append(self.q1.popleft())
        # swap values in q1 & q2
        self.q1, self.q2 = self.q2, self.q1

        # return topVal
        return topVal

    def empty(self) -> bool:
        # return if length of q1 is 0
        return len(self.q1) == 0        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()