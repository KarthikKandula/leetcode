class Solution:
    """
    a bit better optimized solution

    we can bypass using multiple array altogether by using hashmap for storing answers 
        rather than use extra memory for the arrays
        if a value doesn't exist in the hashmap, it means there's no greater element for that number
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create hashmap to record next greater elements for nums2
        hashmap = {}

        # monotonic decreasing stack for nums2
        stack = [] # insert indexes

        # loop thru each element in nums2
        for i, v in enumerate(nums2):
            # remove lower values from stack 
            while stack and v > nums2[stack[-1]]:
                # remove from stack
                popVal = stack.pop()

                # update for the removed value 
                hashmap[nums2[popVal]] = v

            # insert into stack
            stack.append(i)

        # return list of values from hashmap or -1 for each number from nums1
        return [hashmap.get(i, -1) for i in nums1]

    """
    My solution

    we can use monotonic stack and hashmap to solve the problem
        use hashmap to track indexes from nums1
            populate hashmap with values & their indexes from nums1
        loop thru nums2 to populate ans2 to find next greater element for each element
            update index in hashmap to match to nums2 indexes
        loop thru nums1 again to populate correct values into ans array
            fetching from indexes from hashmap
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create hashmap to track values & indexes in nums1
        hashmap = {v:i for i, v in enumerate(nums1)}

        # arrays to store answers i.e next greater elements
        ans = [-1] * len(nums1) # for nums1
        ans2 = [-1] * len(nums2) # for nums2

        # monotonic decreasing stack for nums2
        stack = [] # insert indexes

        # loop for each value in nums2
        for i, v in enumerate(nums2):
            # remove values from stack 
            while stack and v > nums2[stack[-1]]:
                # remove from stack
                popVal = stack.pop()

                # update for the removed value 
                ans2[popVal] = v

            # insert into stack
            stack.append(i)

            # update index if value exists in hashmap
            if v in hashmap:
                hashmap[v] = i

        # loop for each value in nums1 to update values in ans
        for i, v in enumerate(nums1):
            ans[i] = ans2[hashmap[v]]

        # return answer
        return ans