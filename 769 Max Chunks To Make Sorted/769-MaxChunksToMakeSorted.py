class Solution:
    """
    we can solve this problem using basic math
        the problem is asking to partition the input array in such a way that
            individual partitions when sorted & concatenated should form the overall sorted array
        since the input only ranges from [0, n - 1]
            using basic math, to make partitions at any location the max value seen until that point should be equal to the index
            if it's not equal, it means we need to wait until that index to make a partition
            once we have a scenario where the max value is same as the index
                a partition can be made at that location
    """
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # result variable
        res = 0

        # variable to record max value at each location
        tempMax = 0

        # loop thru input arr
        for i, v in enumerate(arr):
            # get max value at this location
            tempMax = max(tempMax, v)

            # check if max value is same as current index
            if tempMax == i:
                res += 1 # increment result since we can make a partition at this location

        # return result
        return res
