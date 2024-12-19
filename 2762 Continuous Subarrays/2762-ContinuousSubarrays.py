class Solution:
    """
    use sliding window & two pointers to solve the problem
        the condition is to count the num of subarrays with diff btwn max and min values less than or equal to 2
        since it's asking for subarrays in an array -- it's a sliding window problem
            since the window length is variable, it's a varible sliding window problem 
            we should use two pointers

        we need to maintain min & max values all the time for the current window
            to do this we use two deques
                minQ - stores indexes of elements in increasing order of their values
                    so that nums[minQ[0]] is always smallest value in the window
                maxQ - stores indexes of elements in decreasing order of their values
                    so that nums[maxQ[0]] is always largest value in the window

        if the diff btwn max & min values (always in front of deques) exceeds 2
            increment left pointer
            remove any indexes from deque that are out of window

        for each window, num of subarrays between l and r is r - l + 1
    """
    def continuousSubarrays(self, nums: List[int]) -> int:
        # left pointer
        left = 0

        # result value
        res = 0

        # create two queues to store min & max values 
        minQ, maxQ = deque(), deque()

        # loop thru every number in nums with the right pointer
        for right in range(len(nums)):
            # handle values in min queue & max queue to make sure they are in order
            while minQ and nums[minQ[-1]] >= nums[right]:
                minQ.pop()

            while maxQ and nums[maxQ[-1]] <= nums[right]:
                maxQ.pop()

            # insert current right pointer value into queues
            minQ.append(right)
            maxQ.append(right)

            # check if condition is broken
            while nums[maxQ[0]] - nums[minQ[0]] > 2:
                # increment left pointer
                left += 1

                # remove out of bounds values from either queues
                if minQ[0] < left:
                    minQ.popleft()
                
                if maxQ[0] < left:
                    maxQ.popleft()
            
            # calculate the no. of subarrays in current window
            res += (right - left + 1)

        # return result val
        return res
