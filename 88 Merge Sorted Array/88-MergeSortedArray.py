class Solution:
    """
    solve this problem using two pointers but with a twist
        it's about comparing two numbers & sorting an array
        instead of doing it from start, better to do it from last to first
            offers flexibility & a bit neat code
        start two pointers at ends of each array
        start another pointer that tracks that current value to be replaced
        compare two pointer value & place the largest value at last pointer
            decrement accordingly
        once all values are processed, sorted array is in 1st input
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # create two pointers at the end of each input 
        i, j = m - 1, n - 1
        last = m + n - 1 # create another pointer at the end of combined inputs

        # loop while j is greater than or equal to 0
        while j >= 0:
            # if i value is greater than j value
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[last] = nums1[i] # place i value at last pointer
                i -= 1 # decrement i value since it's processed
            # if j value is greater than i value
            else:
                nums1[last] = nums2[j] # place j value at last pointer
                j -= 1 # decrement j pointer since it's processed

            # decrement last pointer
            last -=1
        
        # return nums1 array
        return nums1
