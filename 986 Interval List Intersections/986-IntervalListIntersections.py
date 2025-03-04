class Solution:
    """
    This solution uses merge intervals logic a bit
        we need to find overlapping intervals
        so we use two pointers in each input & traverse thru each input
            comparing the values from both lists to each other
        get the max value of min values & min value of max values for each comparision
            only insert into result if they're valid aka l <= r
        keep moving either i or j pointer based on
            if i max value is less -- move i pointer
            if j max value is less -- move j pointer
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # pointers for each list
        i, j = 0, 0
        # get length of each input
        n, m = len(firstList), len(secondList)

        res = [] # result array

        # loop while both pointers are in bounds
        while i < n and j < m:
            # get the left value for new interval
            l = max(firstList[i][0], secondList[j][0])
            # get the right value for new interval
            r = min(firstList[i][1], secondList[j][1])

            # check if this interval value is valid aka left is less than right
            if l <= r:
                # if condition satisfies, append result
                res.append([l, r])
            
            # check if i max is less than j max
            if firstList[i][1] < secondList[j][1]:
                # increment i pointer
                i += 1
            # if j max is less than i max
            else:
                # increment j pointer
                j += 1
        
        # return result array
        return res


    """
    My solution -- working

    same concept as above but with more code
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # pointers for each list
        i, j = 0, 0
        # get length of each input
        n, m = len(firstList), len(secondList)

        res = [] # result array

        # loop while both pointers are in bounds
        while i < n and j < m:
            # skip values if they're out of each other's values
            # if i max is less than j min -- move i
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
            # if j max is less than i min -- move j
            elif secondList[j][1] < firstList[i][0]:
                j += 1
                continue

            # get new val to insert to result
            res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

            # if next i val has conflicts w/ j -- move i pointer
            if i + 1 < n and secondList[j][1] >= firstList[i + 1][0]:
                i += 1
                continue

            # if next j val has conflicts w/ i -- move j pointer
            if j + 1 < m and firstList[i][1] >= secondList[j + 1][0]:
                j += 1
                continue

            # if no conflicts with anything -- move both pointers
            i += 1
            j += 1
        
        # return result array
        return res
