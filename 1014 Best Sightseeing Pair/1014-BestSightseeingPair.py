class Solution:
    """
    we can solve this using dynamic programming
        the prob desc asks to calculate max value for values[i] + values[j] + i - j where i < j
        we can dissect the formula into the max of values[i] + i + values[j] - j
        we keep track of max values[i] + i in a variable
        calculate values[j] - j for each position & update maxScore accordingly
            one more thing is to only update values[i] + i after values[j] - j along with maxScore is calculated for curr position
            to satisfy condition i < j
    """
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # create variable to track max score 
        maxScore = values[0]
        maxLeft = values[0] # variable to track maxleft value until now

        # loop thru input array from 1st position
        for j in range(1, len(values)):
            # calculate curSum for this num
            curSum = values[j] - j

            # get maxScore until now
            maxScore = max(maxScore, maxLeft + curSum)

            # calc maxLeft for next num
            maxLeft = max(maxLeft, values[j] + j)
        
        # return maxScore
        return maxScore
