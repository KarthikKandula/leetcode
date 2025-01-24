class Solution:
    """
    the idea is to find out the count of each word using Counter
        using maxheap, get the top k elements from heap
        the advantage with heap is that it orders the strings in lexicographical order as well
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # create hashmap with counts for words
        count = Counter(words)

        # insert into maxheap in format (-count, word)
        heap = [(-val, key) for key, val in count.items()]

        # heapify heap
        heapq.heapify(heap)

        # for key, val in count.items():
        #     heapq.heappush(heap, (val, key))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # print(heap)

        # create result array
        res = []

        # pop from heap k times to get the word
        for i in range(k):
            # pop from heap
            _, word = heapq.heappop(heap)

            # append popped word to result
            res.append(word)

        # return result
        return res
