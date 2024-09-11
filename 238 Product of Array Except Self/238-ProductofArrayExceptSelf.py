class Solution:
    """
    Create output array & assign it with 1 for length of nums

    Use a process as prefix sum
        the product of all other elements other than current elements is basically the 
            product of prefixes (elements before it) multiplied by the product of postfixes (elements after it) 
        For this we use two variables to keep track of pre & post products

    prefixes
        assign the prefix value in the current index
        multiply the current nums value with prefix (to use in next index)

    postfixes
        slight modification in logic
        multiply the postfix to current output array index
        multiply the postfix to current nums index (to use in next index)
    
    by the end of postfix loop, output array would have desired values
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create output array - same size as nums
        out = [1] * len(nums)

        # Create pre, post variables
        pre, post = 1, 1

        # loop thru the length of nums
        for i in range(len(nums)):
            out[i] = pre # assign pre value to output array current index
            pre *= nums[i] # now multiply current index nums to pre (to be used for next index)
        
        # loop thru length of nums from back to front
        for i in range(len(nums)-1, -1, -1):
            out[i] *= post # multiply output array current index to post
            post *= nums[i] # now update post by multipling with current index nums to post (to be used for next index)

        # return output array
        return out

    """
    Create output array & use it throught the process to get required result

    First - save the product of prefixes of each element from nums in output
        Do this start -> end
        Initialize pre to 1
        Multiply output element in current index with pre
        Multiply pre with current nums index - to update next element

    Second - multiply product of post fixes to elements in output - it already has prefixes
        Do this end -> start
        Initialize post to 1
        Multiply output element in current index with post
        Multiply post with current nums index - to update next element
        Decrease index by 1
    """
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # Create output array - same size as nums
    #     out = [1]*len(nums)
    #     # Create pre, post variables
    #     pre, post = 1, 1

    #     # Prefix processing
    #     for i, x in enumerate(nums):
    #         out[i] *= pre # Multiply out element with pre
    #         pre *= nums[i] # Multiply pre with nums to update next element
    #     print(out)

    #     # Postfix processing
    #     i = len(nums) - 1 # Initialize i with len - 1
    #     while i >= 0:
    #         out[i] *= post # Multiply out element with post
    #         post *= nums[i] # Multiply post with nums to update next element

    #         i -= 1 # Decrease i in each loop

    #     return out