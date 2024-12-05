class DetectSquares:

    def __init__(self):
        # create hashmap to store counts for each point
        self.ptsCount = defaultdict(int)
        self.pts = [] # array to store points

    def add(self, point: List[int]) -> None:
        # increase count for input point
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point) # append point to array

    """
    the first condition for a square to be formed by two different points is that they're diagonal to each other
        for diagonal points, the diff of x & y values is equal
        once we find a diagonal points, we need to find the other two points to complete forming a square
        to find these other points
            we can interchange x & y values from each points to see if they exist in hashmap
            ex: x1, y1 & x2, y2 (diagonal points found) --> x1, y2 & x2, y1 (new points to be found)
            if those points exist, we can mutiply their counts to get the no. of squares that can be formed
    """
    def count(self, point: List[int]) -> int:
        # create result array
        res = 0

        # get query points into different variables -- for ease of use
        qx, qy = point

        # loop thru every point to find diagonal points to query points
        for x, y in self.pts:
            # check if difference between x & y values is equal -- condition for diagonal points
            # check if any x/y value is equal since area should be more than 0
            if abs(qx - x) != abs(qy - y) or x == qx or y == qy:
                continue
            
            # if a point is found, check if other 2 points exist by interchanging x, y values
            # if reaches this point, a diagonal point is found
            # now, find the other two points & add their count to result
            res += self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)]

        # return result
        return res



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)