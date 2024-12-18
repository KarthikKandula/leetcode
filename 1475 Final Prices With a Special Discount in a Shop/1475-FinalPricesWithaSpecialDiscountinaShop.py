class Solution:
    """
    Stack solution

    we can solve this problem using stack (monotonic stack)
        since we need to find the lowest index that satisfies a condition
        we can insert indexes into the stack instead of the actual values
        update values in the input array when the latest value from stack is greater than the current loop value
    
    loop thru input array
        check if last value in stack is greater than or equal to the current looped value
            if it is, reduce the value by the current looped value
        insert current index into the stack
    
    once all elements have been visited, answer array is saved in the input array
    """
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i in range(len(prices)):
            # loop thru stack & check if last value is greater than current value
            while stack and prices[stack[-1]] >= prices[i]:
                # pop from stack & update that index
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        
        return prices


    """
    Own solution
    """
    # def finalPrices(self, prices: List[int]) -> List[int]:

    #     for i in range(len(prices)):
    #         for j in range(i + 1, len(prices)):
    #             if prices[j] <= prices[i]:
    #                 prices[i] = prices[i] - prices[j]
    #                 break
        
    #     return prices
