class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        levels = ["Thousand", "Million", "Billion"]

        # first get under hundreds out the way
        result = self.numberToWordsHelper(num % 1000)

        num = num // 1000

        # then process thousands
        # then process millions --> if number exists
        # them process billions --> if number exists
        for i in range(len(levels)):
            if num > 0 and num % 1000 > 0:
                result = self.numberToWordsHelper(num % 1000) + levels[i] + " " + result
            num = num // 1000
        
        return result.strip()

    def numberToWordsHelper(self, num: int) -> str:
        # takes a number & returns string -- max allowed is 3 digits at max

        # Arrays to store words for numbers less than 10, 20, and 100
        below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""

        # 100's processing
        # if number is greater than 99
        if num > 99:
            result += below_ten[num // 100] + " Hundred "

        # mod num with 100 -> reduces to tens place
        num = num % 100

        # 10's processing
        # if between 20 - 9
        if num < 20 and num > 9:
            # get from array above
            result += below_twenty[num - 10] + " "
        else:
            # if greater than 20
            if num >= 20:
                # get from below hundred
                result += below_hundred[num // 10] + " "
            
            num = num % 10

            # 1's processing
            if num > 0:
                # get from below ten 
                result += below_ten[num] + " "

        return result
