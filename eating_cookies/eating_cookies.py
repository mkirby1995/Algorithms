#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
      ways_to_eat = [1, 2, 3]
      ways = []
      if n ==0:
          return 0
      else:
          for i in ways_to_eat:
              for j in range(i, n + 1):
                  if i * (n // j) != n:
                      print(f"Can eat {i} cookies {n // j} times and {i - 1} cookies {(n) // j} times")
                      print(f"For a total of {i * (n // j) + (i - 1) * ((n) // j)} cookies")
                      if i * (n // j) + (i - 1) * ((n) // j) == n:
                          ways.append(1)
                  else:
                      print(f"Can eat {i} cookies {n // j} times")
                      print(f"For a total of {i * (n // j)} cookies")
                      if i * (n // j) == n:
                          ways.append(1)
          return sum(ways)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
