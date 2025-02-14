class Solution:
    """
    optimized approach
    """
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):
            pops = 0
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                pops += 1
            
            pops += 1 if stack else 0

            res[i] = pops

            stack.append(i)
        
        return res

    """
    brute force
    """
    # def canSeePersonsCount(self, heights: List[int]) -> List[int]:
    #     n = len(heights)
    #     res = [0] * n

    #     for i in range(n):
    #         stack = []
    #         maxVal = 0

    #         for j in range(i + 1, n):
    #             # print(i, j, stack)
    #             if not stack or heights[j] > heights[stack[-1]]:
    #                 if maxVal < heights[i]:
    #                     stack.append(j)
    #                     maxVal = max(maxVal, heights[j])
            
    #         res[i] = len(stack)

    #     return res
