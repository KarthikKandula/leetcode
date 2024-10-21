# 355. Design Twitter

1 possible solution for this problem  

## Method 1

To solve the Twitter problem, we use a combination of a heap and hashmaps. Here's how the solution is structured:

### Data Structures

- **Heap**: Used to efficiently retrieve the latest tweets (max-heap, simulated by negating values).
- **Followers HashMap**: Stores the follow relationships where the keys are `followerId` and the values are sets of `followeeIds`. Using sets ensures O(1) add and remove operations.
- **Tweets HashMap**: Stores users' tweets. Each user’s tweets are kept as a list in the format `[-time, tweetId]` to keep track of the posting order, with negative time values to simulate max-heap behavior.

### Steps

#### `__init__`
1. Initialize the following data structures:
   - `followers`: A hashmap where each user has a set of followees.
   - `tweets`: A hashmap where each user has a list of tweets in the format `[-time, tweetId]`.
   - `time`: A global variable that decrements with each new tweet to maintain the correct order of tweets.

#### `postTweet(userId, tweetId)`
1. Append the `[-time, tweetId]` to the `tweets` hashmap for the `userId`.
2. Decrement the `time` variable after each post to ensure newer tweets have a smaller (more negative) time value.

#### `getNewsFeed(userId)`
1. Create a max-heap to retrieve the latest tweets.
2. For each followee (including the user themself) in the `followers` hashmap:
   - Get the followee’s latest tweet from the `tweets` hashmap and insert it into the heap in the format `[time, tweetId, followeeId, nextIndex]`.
   - The heap is sorted based on `time` since it's negated for max-heap simulation.
3. While the result array has fewer than 10 tweets and the heap is not empty:
   - Pop the top tweet (latest one) from the heap and append it to the result array.
   - If the followee has more tweets, push the next one onto the heap.
4. Return the result array, which contains the 10 most recent tweets.

#### `follow(followerId, followeeId)`
1. Add the `followeeId` to the `followers` hashmap under the `followerId` set.

#### `unfollow(followerId, followeeId)`
1. Check if the `followeeId` exists in the `followers` set for the `followerId`. If it does, remove the `followeeId`.

### Conclusion

This solution uses efficient data structures to implement each operation in O(log n) or O(1) time, depending on the operation. The heap ensures that retrieving the latest tweets is optimized, while hashmaps allow quick lookups for followers and tweets.


### Self Notes
To solve this problem, we use a heap, since a heap always has it's elements in sorted order, add & pop operations happen in log(n) time. python has minheap implementation, so we negate the values to simulate a maxHeap.

__init__
according to the problem statment, we need to keep track of tweets & followers, create a hashmap for followers -- make the values sets since add & remove ops are O(1), create a hashmap for tweets, also need to keep track of the order in which they're received, insert in format - [-time, tweetId]

postTweet
append time & tweetId to tweets hashmap for current user, decrement time after -- for future tweets

getNewsFeed
use a maxHeap with additional values to implement this operation. loop thru the followee's current users in follower hashmap, get each followee's latest tweet & add it to heap, append to heap in format [time, tweetId, followeeId, next index in tweet map]. loop while result array length is less than 10, pop value from heap -- since negated will get latest value, add it to result array, check if that follower has any more tweets left, if they do, add to heap -- will be automatically sorted since already heapified. after loop has finished running, all tweets will be in result array, return it

follow
add followeeId to the current followerId in followers hashmap

unfollow
check if followeeId exists for current followerId in followers hashmap, if it does, remove followeeId

```
__init__
"""
   according to the problem statment, we need to keep track of tweets & followers
      create a hashmap for followers -- make the values sets since add & remove ops are O(1)
      create a hashmap for tweets
         also need to keep track of the order in which they're received
         insert in format - [-time, tweetId]
               -ve to simulate maxHeap in python
"""

postTweet
"""
   posting a tweet is a straightforward operation
      append time & tweetId to tweets hashmap for the user
      decrement time after -- for future tweets
"""

getNewsFeed
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

follow
"""
   following a user is a straightforward operation
      add followeeId to the current followerId in followers hashmap
"""

unfollow
"""
   unfollowing a user is a straightforward operation
      check if followeeId exists for current followerId in followers hashmap
         if it does, remove followeeId
"""
```
