class Solution:
    """
    Another solution (using heap)

        Use a hashmap to count elements
        For all elements in hashmap, insert into heap in a way as (-count, value)
            -count since python implements minheap, so -ve'ing it makes it max heap
        now, pop from heap k times
    """
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     hashmap = {}
    #     # count = [[]] * (len(nums) +1)
    #     heap = [] 

    #     for i in nums:
    #         hashmap[i] = 1 + hashmap.get(i, 0)

    #     for l, v in hashmap.items():
    #         heapq.heappush(heap, (-v, l))

    #     res = []
    #     while len(res) < k:
    #         res.append(heapq.heappop(heap)[1])
        
    #     return res

    """
    NeetCode solution - o(n)

        Use a hashmap to count elements
        Use a count array (of size len(nums)+1), to keep record the amount of time elements repeat via indexes
        Iterate thru the count array in desc order, append to new result array, if length is as k, return result array 
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        # count = [[]] * (len(nums) +1)
        count = [[] for i in range(len(nums)+1)]

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        for l, v in hashmap.items():
            count[v].append(l)

        res = []
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                res.append(n)

                if len(res) == k:
                    return res

    """
    My nlogn solution
    """
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     hashmap = {}

    #     for i in nums:
    #         hashmap[i] = 1 + hashmap.get(i, 0)
        
    #     # print(hashmap)

    #     sortedCountS = sorted(hashmap.values(), reverse=True)

    #     # print(sortedCountS)

    #     # print(sortedCountS[:k])

    #     out = []
    #     for x in hashmap:
    #         if hashmap[x] in sortedCountS[:k]:
    #             out.append(x)

    #     # print(out)

    #     return out