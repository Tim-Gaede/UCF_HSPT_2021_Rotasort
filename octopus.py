# 2021 UCF HSPT - Octopus
# Author: Josh Delgado

"""
To solve this problem, you can make a few observations that make this a lot simpler

First major observation:
A single wave is equivalent to you moving an element to any position you desire.

As a result, you are now guaranteed that the number of waves is <= n
since you can move the lowest element to the first position, the second lowest
to the second position, etc.

However, you can be more efficient by keeping some shell static, and moving 
the others between them.

For example for the array:
4 5 2 1 3 6

You could choose 1, 3, and 6 to move the others around
So you would move 2 between the 1 and 3, then move 4 & 5 between 3 and 6.
Thus you would only move 3 shells (2, 4, 5)


Another observation from this:
The ones you keep static have to be in increasing order since you can't
re-arrange the ones you're keeping static (since you're keeping it static)

So now the problem is "which shells should I keep in place"? The more
I keep static, the less I move, so I want to maximize the number I keep in place

So in other words, you want an increasing sequence of shells that you pick
to stay static and not move, and you want to maximize the length. This is a problem 
referred to as the Longest Increasing Subsequence, and you can do this in O(NlogN)

So the number you move is the total - length(Longest Increasing Subsequence)

"""


# Gets the Longest Increasing Subsequence length in O(nlogn)
def LIS(arr):
  n = len(arr)
  
  # infinity
  inf = 2_000_000_000

  # Stores the minimum value of the subsequence of length[index]
  # lastElement[1] = the minimal value of the last element 
  # of an increasing sequence of length 1
  lastElement = [inf for i in range(n+1)]
  lastElement[0] = -inf

  for val in arr: 
    # Binary search for the first value in lastElement that is strictly greater than me
    lo = 0 
    hi = n
    while lo < hi: 
      mid = (lo+hi)//2
      if (lastElement[mid] > val):
        # Then we could use this
        hi = mid
      else:
        # The lastElement is too low, increase it
        lo = mid+1

    # Update the lastElement if it's better
    if (lastElement[lo-1] < val and val < lastElement[lo]):
      lastElement[lo] = val

  longestLen = 0
  for i in range(n+1):
    if lastElement[i] < inf:
      longestLen = i
  
  return longestLen


if __name__ == "__main__":
  numTests = int(input())

  for test in range(numTests):
    # Take in input
    n = int(input()) 
    arr = [int(i) for i in input().split(" ")] 

    # Get the length of the longest increasing subsequence
    longestIncreasingSubsequenceLength = LIS(arr) 

    # The number we change is the total length - LISLength
    print(n - longestIncreasingSubsequenceLength)