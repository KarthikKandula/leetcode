class Solution:
    """
    optimized solution

    same logic using monotonic decreasing stack 
        but looping twice using 2 * n
        to loop over numbers from starting again
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums) # get length of input in a variable
        res = [-1] * n # create result array for length on input

        # stack to implement monotonic decreasing stack
        stack = [] # stores index

        # loop for twice the length of input
        for i in range(n * 2):
            # if i > n - 1:
            #     i = (i - 1) % n

            # modulo i value to get correct index val
            i = i % n

            # remove from stack
            while stack and nums[i] > nums[stack[-1]]:
                popVal = stack.pop() # pop latest value from stack
                res[popVal] = nums[i] # update the result for popped value -- since next greater value has been found

            # insert into stack
            stack.append(i)

        # return result
        return res

    """
    brute force solution
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [-1] * n

        for i in range(n):

            for j in range(i + n):
                if i != 0 and j > n - 1:
                    j = j % i

                # print(i, j)
                if nums[j] > nums[i]:
                    res[i] = nums[j]
                    break

        return res

