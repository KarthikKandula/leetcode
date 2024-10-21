class Solution:
    """
    we use heap & queue to solve this problem
        count the occurences for each task in the input
        insert only counts (values) into the heap -- negate them so it's max heap
        create a queue -- to record values that will be inserted back into the heap
        create a variable that keeps track of time

    loop while heap or queue has values
        pop values from heap
            reduce count by 1 -- since using one time interval
            increment time by 1
            insert into queue if count is not 0 in format - [count, time this can be inserted back into heap (time + n)]
        check if first value in queue can be inserted at current time
            insert if true

    once loop is done, return time variable 
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count occurences in tasks
        count = Counter(tasks)

        # create an array with -ve values
        maxHeap = [-cnt for cnt in count.values()]
        # heapify above array
        heapq.heapify(maxHeap)

        # variable to keep track of time/intervals
        time = 0
        queue = deque()

        # loop while heap has values or queue has values
        while maxHeap or queue:
            # increment time value for current loop
            time += 1 # if in case has to stay idle, time is incremented

            # if values exists in heap
            if maxHeap:
                # pop from heap -- get the most frequent value for current loop
                tempCnt = heapq.heappop(maxHeap)
                tempCnt += 1 # add one to the count -- reducing the count for this task

                # check if tempCnt is 0, if it is we've used all tasks for this letter
                if tempCnt != 0:
                    # if tempCnt has a value, append to queue since need to process in future
                    queue.append([tempCnt, time + n]) # add in format [tempCnt, time at which can be added to heap]

            # insert values from queue into heap
            # check if queue has values & queue's first value's time is same as current time
            if queue and queue[0][1] == time:
                # push into heap the count value
                heapq.heappush(maxHeap, queue.popleft()[0])

        # return time value
        return time
