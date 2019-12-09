#!/usr/bin/python

import argparse

def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = 0
    profits = []
    for i in prices:
        if i <= current_min_price_so_far:
            current_min_price_so_far = i
        max_profit_so_far = i - current_min_price_so_far
        profits.append(max_profit_so_far)
    return max(profits)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
