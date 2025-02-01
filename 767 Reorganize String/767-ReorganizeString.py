class Solution:
    """
    this problem uses heaps & string counting 
        the basic idea is to place the longest occuring char in alternative positions
            and the same to others as well
        after getting the count of each letter
        check if a string can be formed
            if any char appears more than half times, it's impossible
        if it passes the check
            create an array/empty string
            create a maxheap, insert values in format (-val, char)
            pop value from the heap, compare with last value 
                if same value is popped
                pop another value & insert this value into result
                reinsert first value into heap
        after all values have been processed, the string is formed
    """
    def reorganizeString(self, s: str) -> str:
        # get counts of each letter
        counter = Counter(s)

        # get length of input
        n = len(s)

        # If any character appears more than (n + 1) // 2 times, it's impossible to rearrange
        if any(count > (n + 1) // 2 for count in counter.values()):
            return "" # return empty string

        # array to store result -- will be joined in the end
        res = []
        # populate array -- will become heap
        maxHeap = [(-val, char) for char, val in counter.items()]
        heapq.heapify(maxHeap) # heapify

        # loop while heap is populated
        while maxHeap:
            # pop value from heap
            firstCount, firstChar = heapq.heappop(maxHeap)
            # if result isn't populated yet or last char from result isn't the current first
            if not res or firstChar != res[-1]:
                # insert into res
                res.append(firstChar)

                # update count
                firstCount += 1

                # if count isn't 0, insert back into heap
                if firstCount != 0:
                    heapq.heappush(maxHeap, (firstCount, firstChar))

            # process second latest char
            else:
                # pop value from heap
                secondCount, secondChar = heapq.heappop(maxHeap)

                # insert into res
                res.append(secondChar)

                # update count
                secondCount += 1

                # if count isn't 0, insert back into heap
                if secondCount != 0:
                    heapq.heappush(maxHeap, (secondCount, secondChar))
                
                # insert first char back into heap, to be processed in next iteration
                heapq.heappush(maxHeap, (firstCount, firstChar))

        # return values from array joined together
        return ''.join(res)


    def reorganizeString(self, s: str) -> str:
        # count = Counter(s)

        counter = {}

        maxVal = 0

        for c in s:
            counter[c] = 1 + counter.get(c, 0)

            maxVal = max(maxVal, counter[c])

        # print(counter, maxVal)

        n = len(s)
        mid = n // 2

        if n % 2: # if odd
            if maxVal > mid + 1:
                return ""
        else: # if even
            if maxVal > mid:
                return ""

        maxHeap = [(-val, char) for char, val in counter.items()]

        minHeap = []

        heapq.heapify(maxHeap)
        heapq.heapify(minHeap)

        letters = len(counter)

        res = ""

        i = 0

        while i < n:
            # pop from maxHeap
            count, c = heapq.heappop(maxHeap)

            # add to result
            res += c

            count = abs(count)
            count -= 1

            # if count is 0, delete
            if count == 0:
                del counter[c]

            # insert into minHeap
            if count > 0:
                heapq.heappush(minHeap, (i + 2, c, count))

            # print(i, maxHeap, minHeap)

            # if condition matches, pop from minheap & insert into maxheap
            while minHeap and minHeap[0][0] <= i + 1:
                index, char, num = heapq.heappop(minHeap)

                heapq.heappush(maxHeap, (-num, char))

            i += 1

        return res

