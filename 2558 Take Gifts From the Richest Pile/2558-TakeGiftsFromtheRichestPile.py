class Solution:
    """
    Optimized solution

    same as own solution but better code
    """
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # reassign gifts array by negating numbers
        gifts = [-x for x in gifts]

        # heapify gifts array
        heapq.heapify(gifts)

        # loop while k is not 0
        while k:
            # pop from heap -- since this is maxHeap, gets highest num first
            val = heapq.heappop(gifts)

            # push into heap the squareroot of above popped number
            heapq.heappush(gifts, -math.isqrt(abs(val)))

            # decrement k
            k -= 1

        # return the sum of values in gifts array/heap
        return -sum(gifts)

    """
    Own solution

    solve this problem using maxHeap
        maxHeap is minHeap but with values negated
            always gets the max value from the array
        the idea is to use the max value at any time, replace the value with sqrt value
    """
    # def pickGifts(self, gifts: List[int], k: int) -> int:
    #     # create maxHeap -- minHeap implementation with negated no.s
    #     maxHeap = []

    #     # get total of the input array -- to track total
    #     total = sum(gifts)

    #     # loop thru input gifts & insert into heap
    #     for i, v in enumerate(gifts):
    #         maxHeap.append([-v, i])

    #     # heapify heap
    #     heapq.heapify(maxHeap)

    #     # loop while k is not 0
    #     while k != 0:
    #         # pop from heap -- gets the max value
    #         val, ind = heapq.heappop(maxHeap)

    #         # calculate sqrt value for popped number
    #         diff = floor(math.sqrt(abs(val)))

    #         # subtract the remaining value from total
    #         total -= (abs(val) - diff)

    #         # push sqrt value back into queue
    #         heapq.heappush(maxHeap, [-diff, ind])

    #         # decrement k
    #         k -= 1

    #     # return total
    #     return total
