#!/usr/bin/python

import sys

def rps_helper(arr, n):
  if len(arr) == n:
    return arr
  else:
    return *rps_helper(arr + ['rock'], n), *rps_helper(arr + ['paper'], n), *rps_helper(arr + ['scissors'], n)


def rock_paper_scissors(n):
  answer = []
  bank = rps_helper([], n)
  for _ in range((3)**n):
    answer.append(list(bank[0:n]))
    bank = bank[n:]
  return answer


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')