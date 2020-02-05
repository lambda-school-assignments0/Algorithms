#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Brute force method:
  profit_max = prices[1] - prices[0]

  for price_low_idx in range(0, len(prices)):
    for price_high_idx in range(price_low_idx + 1, len(prices)):
      if (prices[price_high_idx] - prices[price_low_idx]) > profit_max:
        profit_max = prices[price_high_idx] - prices[price_low_idx]

  return profit_max


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))