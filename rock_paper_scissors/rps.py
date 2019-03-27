#!/usr/bin/python

import sys


def helper(list, n):
    if n == 0:
        return [list]
    return helper([*list, "rock"], n-1) + helper([*list, "paper"], n-1) + helper([*list, "scissors"], n-1)


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    return helper([], n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
