class Solution:
    """
    Found solution
    use sort() to sort nums as strings in descending order (reverse=True).
        The key function for sorting is lambda x: x*10.
            the idea is to "extend" the string by repeating it 10 times, ensures the correct order during sorting
            Since max possible digit length of numbers in nums is 10 (as per constraints)
            repeating string 10 times ensures all possible concatenation orders are correctly represented
    """
    def largestNumber(self, nums: List[int]) -> str:
        # convert input into string using map function
        nums = list(map(str, nums))

        # sort nums array by multiplying each string 10 times
        # makes it easy to determine which string comes first, acc to problem constraints
        nums.sort(key = lambda x: x*10, reverse=True)

        # after array is sorted, return the string joined by all values in list
        # if 1st value is 0, it means the nums are 0
        return "".join(nums) if nums[0] != "0" else "0" 

    """
    NeetCode solution

    custom comparator (compare) determines the order in which two numbers should appear to form the largest possible number
        comparison is based on string concatenation
            If n1 + n2 is greater than n2 + n1 --> n1 should come before n2.
                Otherwise, n2 should come before n1.
    
    Why n1 + n2 > n2 + n1?
        This checks the concatenated result of placing n1 before n2 versus placing n2 before n1
        By choosing the order that produces the larger concatenated result, we ensure the largest possible number is formed
        
        Returning -1 or 1:
        In Python's sorted(), a comparator must return
            -1 if the first element is smaller,
            1 if the second element is smaller.
            Returning -1 ensures that n1 comes before n2 in the sorted list.
    """
    def largestNumber(self, nums: List[int]) -> str:
        # convert each value to str
        for i, v in enumerate(nums):
            nums[i] = str(v)
        
        # custom compare function --> also called comparator
        def compare(n1, n2):
            # return n1 + n2 > n2 + n1
            # check for below condition
            if n1 + n2 > n2 + n1:
                return -1 # send -1 to indicate true -- n1 comes before n2
            else:
                return 1 # send 1 to indicate false -- n2 comes before n1

        # using sorted to call custom comparator func
        nums = sorted(nums, key = cmp_to_key(compare))

        # return a string of all values joined in nums
        # converting to int & then to str to handle 0's
        return str(int("".join(nums)))
