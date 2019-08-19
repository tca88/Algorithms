#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    result = []
    def helper(current_round, answer=[]):
        if current_round == 0:
            #append result to the answer array
            result.append(answer)
            return
        for play in plays:
            helper(current_round-1, answer + [play])
        
    helper(n, [])
    return result

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')