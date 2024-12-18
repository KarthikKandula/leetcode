class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # helper function
        def gain(noPass, noActual):
            return ((noPass + 1) / (noActual + 1)) - (noPass / noActual)
        
        sumAvg = 0.0
        maxHeap = []

        # insert values into heap
        for i, val in enumerate(classes):
            tPass, tAct = val[0], val[1]
            sumAvg += tPass / tAct
            maxHeap.append([-gain(tPass, tAct), i])

        heapq.heapify(maxHeap)

        # process values from heap
        while extraStudents:
            # pop from heap
            gainP, index = heapq.heappop(maxHeap)

            sumAvg -= classes[index][0] / classes[index][1]

            # add one to values in input classes
            classes[index] = [classes[index][0] + 1, classes[index][1] + 1]

            sumAvg += classes[index][0] / classes[index][1]

            # insert updated value into heap
            heapq.heappush(maxHeap, [-gain(classes[index][0], classes[index][1]), index])

            extraStudents -= 1

        return sumAvg / len(classes)
