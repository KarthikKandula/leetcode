class Twitter:
    """
    according to the problem statment, we need to keep track of tweets & followers
        create a hashmap for followers -- make the values sets since add & remove ops are O(1)
        create a hashmap for tweets
            also need to keep track of the order in which they're received
            insert in format - [-time, tweetId]
                -ve to simulate maxHeap in python
    """
    def __init__(self):
        # create variables to hold time, follwerMap, tweetMap
        self.time = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list) # values in format [-time, tweetId]

    """
    posting a tweet is a straightforward operation
        append time & tweetId to tweets hashmap for the user
        decrement time after -- for future tweets
    """
    def postTweet(self, userId: int, tweetId: int) -> None:
        # add tweetid, with count to tweetMap
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1 # decrement time, since simulating a max heap

    """
    this is a bit of a complicated operation
        we use a maxHeap with additional values to implement this
    
    we only need to get 10 latest tweets for all followers of current user
        self is also considered a follower, so add to follwer hashmap before hand

    loop thru the followee's of current user in follower hashmap
        get each followee's latest tweet & add it to heap
        append to heap in format [time, tweetId, followeeId, next index in tweet map]

    loop while result array length is less than 10
        pop value from heap -- since negated will get latest value
        add it to result array
        check if that follower has any more tweets left
            if they do, add to heap -- will be automatically sorted since already heapified
    
    after loop has finished running, all tweets will be in result array, return it
    """
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # array to hold result
        heap = [] # array will become heap

        # add self to followerMap since useful to retrieve self's tweets
        self.followerMap[userId].add(userId)

        # get latest tweets from all following users
        # loop thru each followee for current user
        for eachFollowee in self.followerMap[userId]:
            # get latest tweet for each followee
            # get max index in tweets for current followee
            tempIndex = len(self.tweetMap[eachFollowee]) - 1 # -1 to adjust for array indices
            
            if tempIndex >= 0:
                # get time & tweetId of latest tweet
                tempTime, tempTweetId = self.tweetMap[eachFollowee][tempIndex]
                
                # insert into heap with below data
                heap.append([tempTime, tempTweetId, eachFollowee, tempIndex - 1])
        
        # heapify above array
        heapq.heapify(heap)
        
        # loop thru heap & get 10 latest values -- might have to add values to heap
        while heap and len(res) < 10:
            # pop from heap -- get the highest latest value
            tempTime, tempTweetId, tempFollowee, tempIndex = heapq.heappop(heap)
            res.append(tempTweetId) # append above tweetId to result array

            # check if current followee has any more tweets:
            if tempIndex >= 0:
                # get time & tweetId of latest tweet
                tempTime, tempTweetId = self.tweetMap[tempFollowee][tempIndex]
                
                # insert into heap with below data
                heapq.heappush(heap,[tempTime, tempTweetId, tempFollowee, tempIndex - 1])
        
        return res # return result array

    """
    following a user is a straightforward operation
        add followeeId to the current followerId in followers hashmap
    """
    def follow(self, followerId: int, followeeId: int) -> None:
        # add new followeeId to followerMap
        self.followerMap[followerId].add(followeeId) # no worry of duplicates, since a set

    """
    unfollowing a user is a straightforward operation
        check if followeeId exists for current followerId in followers hashmap
            if it does, remove followeeId
    """
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId from followerMap
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)