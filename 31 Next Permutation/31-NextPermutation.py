class Solution:
    """
    this problem can be solved with good understanding of how permutations work
        Permutations are arranged in lexicographical (dictionary) order.
        the rightmost part of the array is the "fastest-changing" part, while the leftmost part changes the slowest.
        The rightmost portion of the array determines the smallest possible changes that can be made to form the next permutation
        To get the next lexicographically larger permutation, you want to change the smallest possible part of the array to ensure it remains as close to the current permutation as possible
    
        since the order of permutations is decided by changing the values towards the end
            we look from the right when this pattern is broken
                the first decreasing element is the point where the next largest permutation can be found
            by finding the value that is immediately next to this value & swapping it
                we form the next higher value
            in the end reverse all values from i to end 
                since for the next permutation, the values always appear in ascending order
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create i pointer at the 2nd last location
        i = len(nums) - 2

        # find the first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # find the element just greater than i
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # swap the element
            self.swap(nums, i, j)
    
        # reverse everything in i + 1
        self.reverse(nums, i + 1)
    
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1

        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
 
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
