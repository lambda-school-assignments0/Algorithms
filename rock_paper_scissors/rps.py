#!/usr/bin/python

import sys

def rock_paper_scissors_helper(arr, n):
  if len(arr) != n:
    return \
    rock_paper_scissors_helper(arr + ['rock'], n), \
    rock_paper_scissors_helper(arr + ['paper'], n), \
    rock_paper_scissors_helper(arr + ['scissors'], n)
  else:
    return arr

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  else:
    return \
      [*rock_paper_scissors_helper([], n)]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')