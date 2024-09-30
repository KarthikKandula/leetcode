class Solution:
    """
    We can use binary search with a good amount of twists to implement a solution
        the intuition is to 

    writeup later
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # create new variables to store arrays
        A, B = nums1, nums2
        # calculate total length -- two arrays combined
        total = len(nums1) + len(nums2)
        half = total // 2 # calculate half of total

        # check if B is longer than A
        if len(B) < len(A):
            A, B = B, A # swap if they are

        # left & right pointers for binary search
        l, r = 0, len(A) - 1 # we only traverse thru A, so r is max of A

        # loop as long as we return a value 
        while True:
            # calculate mid value of A
            mid = (l + r) // 2
            # calculate mid value of B based on half & mid value of A -- this is the remaining of what's left
            Bmid = half - mid - 2 # -2 is to account for the index calculations

            # get Aleft position value -- this is the left most value of the A's left subarray -- default to -inf
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            # get Aright position value -- this is the right most value of the A's right subarray -- default to inf
            Aright = A[mid + 1] if (mid + 1) < len(A) else float("infinity")
            # get Bleft position value -- this is the left most value of the B's left subarray -- default to -inf
            Bleft = B[Bmid] if Bmid >= 0 else float("-infinity")
            # get Bright position value -- this is the right most value of the B's right subarray -- default to inf
            Bright = B[Bmid + 1] if (Bmid + 1) < len(B) else float("infinity")

            # check if A's left is less than B's right & b's left is less than a's right -- if they are then we have the right order
            if Aleft <= Bright and Bleft <= Aright:
                # calculate median
                if total % 2: # if total is odd - since remainder here is 1
                    return min(Aright, Bright)
                else: # if total is even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if it reaches here, it means we don't have the sorted order
            elif Aleft > Bright: # check if Aleft > Bright -- means we have to reduce left since more values in B have to be fitted
                r = mid - 1
            # this condition defaults to Bleft > Aright
            else: # means we have to increase left since more values in A have to be fitted
                l = mid + 1

