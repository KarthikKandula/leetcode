class Solution:
    """
    Use sliding window method to solve the problem
        In this case, window length is limited to the length of s1, since that's the area we're always going to look thru

    Use two hashmaps to keep count of occurences in each inputs

    loop thru the second input 
        check if both hashmaps are equal
        if they aren't, add right pointer value to second hashmap
        remove left pointer value from second hashmap
    
    keep doing it until the end 
        in the end compare both hashmaps one final time & return appropriate values
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if length of s1 > s2, if yes, not possible to solve the problem
        if len(s1) > len(s2): return False

        # Initialize two hashmaps to keep track of counts for s1 & s2
        cnt1, cnt2 = {}, {}

        # loop thru s1 & update count in hashmap, do for s2 too
        for i in range(len(s1)):
            cnt1[s1[i]] = 1 + cnt1.get(s1[i], 0)
            cnt2[s2[i]] = 1 + cnt2.get(s2[i], 0)

        # initialize left pointer
        l = 0

        # loop thru s2 other than the character already looped thru above
        for r in range(len(s1), len(s2)):
            # check if both hashmaps are equal
            if cnt1 == cnt2:
                return True # return true if they are

            # if hashmaps aren't equal, add the next right pointer value to hashmap & update count
            cnt2[s2[r]] = 1 + cnt2.get(s2[r], 0)
            # update left pointer value count in hashmap
            cnt2[s2[l]] -= 1
            if cnt2[s2[l]] == 0: # check if any value in the hashmap is 0, if it is pop that value
                cnt2.pop(s2[l])

            l += 1 # increment left pointer

        # check if hashmaps are equal one last time & return appropriate values
        if cnt1 == cnt2:
            return True
        else:
            return False


