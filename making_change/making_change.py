#!/usr/bin/python

import sys

def making_change(amount, denominations):
  ### Recursive solution
  # ¯\_(ツ)_/¯
  
  ### Dynamic programming w/ matrix
  # Initialize 'bank'
  bank = [[0 for _ in range(amount + 1)] for _ in range(len(denominations) + 1)]
  # Initialize base case
  bank[0][0] = 1
  bank[1][:] = [1 for _ in range(amount + 1)]
  # Calculate number of ways to make change
  for row in range(2,len(bank)):
    for col in range(len(bank[0])):
      if col >= denominations[row-1]:
        bank[row][col] = bank[row][col-denominations[row-1]] + bank[row-1][col]
      else:
        bank[row][col] = bank[row-1][col]

  return bank[-1][-1]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")