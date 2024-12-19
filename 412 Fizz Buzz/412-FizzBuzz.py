class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # result array
        res = []

        # loop between 1 & n + 1 -- to include n
        for i in range(1, n + 1):
            # temp variable to calculate remainders
            temp3 = i % 3
            temp5 = i % 5

            # check for conditions & insert into result array accordingly
            if temp3 == 0 and temp5 == 0:
                res.append('FizzBuzz')
            elif temp3 == 0:
                res.append('Fizz')
            elif temp5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        
        # return result array
        return res
