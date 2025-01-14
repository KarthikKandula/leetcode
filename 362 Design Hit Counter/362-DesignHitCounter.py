class HitCounter:

    def __init__(self):
        # insert in format (t, c)
        self.hits = [[0, 0] for _ in range(300)]

    def hit(self, timestamp: int) -> None:
        # get prorated index by % 300
        i = timestamp % 300
        # get prorated values from index
        t, c = self.hits[i]

        # if ith index value is same as timestamp 
        if t == timestamp:
            # increment hit counter
            self.hits[i][1] += 1
        # if not, update timestamp value & hit counter
        else:
            # assign timestamp value
            self.hits[i][0] = timestamp
            # assign hit counter value
            self.hits[i][1] = 1

    def getHits(self, timestamp: int) -> int:
        # intitalize count value to 0
        count = 0

        # loop for 300 values
        for i in range(300):
            # get this value
            t, c = self.hits[i]

            # check if differnce of current index timestamp value is less than 300
            if timestamp - t < 300:
                # increment hit counter value to count variable
                count += c
        
        # return count value
        return count

class HitCounter:

    def __init__(self):
        # queue to hold values in order of appearance
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        # register hit -- aka insert in queue
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # get num of hits by comparing first value in queue with timestamp
        # should be less than 300
        while self.q and timestamp - self.q[0] >= 300:
            # pop first value in queue
            self.q.popleft()

        # return length of queue
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)