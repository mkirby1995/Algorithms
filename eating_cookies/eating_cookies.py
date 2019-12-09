#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
      ways_to_eat = [1, 2, 3]
      ways = [1] + [0] * n
      for i in ways_to_eat:
          for j in range(i, n + 1):
              ways[j] += ways[j - ways_to_eat]
      return ways[n]
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
