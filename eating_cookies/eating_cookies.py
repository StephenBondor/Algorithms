#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# W(0) = 1  (from the base case)
# W(1) = 1  (from the base case)
# W(2) = 2  (from the base case)
# W(3) = W(2) + W(1) + W(0) = 2 + 1 + 1 = 4
# W(4) = W(3) + W(2) + W(1) = 4 + 2 + 1 = 7
# W(5) = W(4) + W(3) + W(2) = 7 + 4 + 2 = 13


def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    o = 1
    p = 1
    q = 2
    ways = 0
    for i in range(n-2):
        ways = o + p + q
        o = p
        p = q
        q = ways
    return ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
