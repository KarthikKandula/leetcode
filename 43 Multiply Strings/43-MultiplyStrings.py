class Solution:
    """
    the idea is to perform basic multiplication but convert it to code
        while performing multiplication for 2 digit or more digit numbers
        we do it in a nested loop formate i.e, multiply each digit with each other
        and after each levels do it so as to skip one level from right

        we achieve the same functionality but by using nested loops
        the functionaly of skipping levels from right can be achieved by adding both indexes
    
    create a result array with max possible length 
        i.e add length of both numbers
    
    reverse both inputs since we'll be processing both values in reverse
    
    create a nested loop to go thru each element for both numbers
        multiply each location values
        insert the product to the result array in [i + j] location -- skipping levels from right
            value to keep in the location is remainder -- %
        if any carry exists, insert in next location [i + j + 1]
            carry is the product of the number -- //
    
    after nested loop is done product is in reverse order in result array
        reverse the array again 
        remove any preceding 0's
    
    convert values to string & generate string to return output
    """
    def multiply(self, num1: str, num2: str) -> str:
        # if a 0 is present in either num's, return 0 -- basic multiplication rules
        if '0' in [num1, num2]:
            return '0'

        # create result array for max length of output
        res = [0] * (len(num1) + len(num2))

        # reverse input to make it easy on ops
        num1, num2 = num1[::-1], num2[::-1]

        # loop thru both inputs for multiplication ops
        for i in range(len(num1)):
            for j in range(len(num2)):
                # calculate product for this location
                digit = int(num1[i]) * int(num2[j])

                # insert this digit into result
                res[i + j] += digit

                # update next digit with carry -- done by retreiving product using //
                res[i + j + 1] += (res[i + j] // 10)

                # update current location with the remainder after appending product to next location
                # replace the value
                res[i + j] = res[i + j] % 10
        
        # result is in reverse order at this point, reverse the array & remove any preceding 0's
        res = res[::-1]
        beg = 0 # pointer to track the beginning point

        # loop while location in result is 0 & beg pointer is less than length
        while res[beg] == 0 and beg < len(res):
            beg += 1 # increment beginning

        # convert each element in result array to string
        res = map(str, res[beg:])

        # return string formed by joining each element in result array
        return "".join(res)
