class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # create & insert values into heap in format (value, index)
        heap = [(val, index) for index, val in enumerate(nums)]
        heapq.heapify(heap) # heapify heap

        # loop while k is more than 0
        while k:
            # pop lowest value from heap
            val, index = heapq.heappop(heap)

            # update the index of popped value from heap from above
            # update directly in nums to not have to update values again
            nums[index] = nums[index] * multiplier

            # push the updated value back into the heap
            heapq.heappush(heap, (nums[index], index))

            # decrement k
            k -= 1
        
        # return nums array -- by this time it is going to be updated
        return nums