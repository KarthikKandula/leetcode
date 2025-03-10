class SparseVector:
    def __init__(self, nums: List[int]):
        # hashmap to store non-zero values
        self.hashmap = {}

        # loop thru input nums
        for i, n in enumerate(nums):
            # if a non-zero number
            if n != 0:
                # save in hashmap
                self.hashmap[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0 # variable to store result

        # loop for each key, value in hashmap
        # if a value exists in vec.hashmap outside the bounds of items in this hashmap, won't matter
        # cuz, it'll be a zero at that point
        for k, v in self.hashmap.items():
            # if this index exists in vec's hashmap
            if k in vec.hashmap:
                # multiply & store in result
                res += v * vec.hashmap[k]

        # return result
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)