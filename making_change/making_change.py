#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # base case
    if amount < 0:
      return 0
    if amount == 1:
      return 1
    waystoMakeChange = [1] + [0] * amount

    for c in denominations:
        for x in range(c, amount + 1):
            waystoMakeChange[x] += waystoMakeChange[x - c]
    return waystoMakeChange[amount]

print(making_change(10, [1, 5, 10, 25, 50]))
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")