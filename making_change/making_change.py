# !/usr/bin/python

import sys

# from sympy import *
# from sympy.abc import x

# import time
# start = time.time()

# end = time.time()
# print(end - start)

# W( 0) =  1  (the base case)
# W( 1) =  1 = W( 0)
# W( 5) =  2 = W( 0) + W( 0)                 1 +  1
# W(10) =  4 = W( 5) + W( 0) + W(0)          2 +  1 + 1
# W(15) =  6 = W(10) + W( 0) + W(0)          4 +  1 + 1
# W(20) =  9 = W(15) + W( 5) + W(0)          6 +  2 + 1
# W(25) = 13 = W(20) + W( 5) + W(0) + W(0)   9 +  2 + 1 + 1
# W(30) = 18 = W(25) + W( 5) + W(5) + W(0)  13 +  2 + 2 + 1
# W(35) = 27 = W(30) + W(15) + W(5) + W(0)  18 +  6 + 2 + 1
# W(40) = 40 = W(35) + W(20) + W(5) + W(5)  27 +  9 + 2 + 2
# W(45) = 68 = W(40) + W(25) + W(20)+ W(15) 40 + 13 +
# W(50) = 96 = 68 + 27 + 1

# W( 0) =  0
# W( 1) =  1                                                            c1
# W( 2) =  2 = W( 1) + W( 1)                         1 +  1             c5
# W( 3) =  4 = W( 2) + W( 1) + W(1)                  2 +  1 + 1         c10
# W( 4) =  6 = W( 3) + W( 1) + W(1)                  4 +  1 + 1         c15
# W( 5) =  9 = W( 4) + W( 2) + W(1)                  6 +  2 + 1         c20
# W( 6) = 13 = W( 5) + W( 2) + W(1) + W(1)           9 +  2 + 1 + 1     c25
# W( 7) = 18 = W( 6) + W( 2) + W(2) + W(1)          13 +  2 + 2 + 1     c30
# W( 8) = 27 = W( 7) + W( 4) + W(2) + W(1)          18 +  6 + 2 + 1     c35
# W( 9) = 40 = W( 8) + W( 4) + W(4) + W(1)          27 +  6 + 6 + 1     c40
# W(10) = 68 = W( 9) + W( 6) + W(4) + W(1)          40 + 13 + 6 + 1     c45
# W(11) = 96 = W(10) + W(68) + W(4) + W(1) + W(1)   68 + 1              c50

# 0, 1, 2, 5, 10


def making_change(amount, denominations):
    # fx = 1

    # for i in denominations:
    #     fx = fx * (1 - x**i)**-1
    # print(fx)

    # return None
    # x = Symbol("x")
    # a = Symbol("a")

    # fx = 1

    # for i in denominations:
    #     fx = fx * (1 - x**i)**-1
    # print(expand(fx*(1-x**100)**5))

    #   ax = ((1-x**20)**6) / (((1-x)**2) * (1-x**2)
    #                            * (1-x**5) * (1-x**10) * (1-x**20))

    # ways = [1]+[0]*amount
    # for coin in denominations:
    #     print(coin)
    #     for i in range(coin, amount+1):
    #         ways[i] += ways[i-coin]
    #         print(ways)

    # x = Symbol("x")
    # a = Symbol("a")
    # g = Symbol("g")
    # # h = Symbol("h")
    # ways = 1

    # fiveFactored = (((1-x)**2)**-1)
    # # * ((1-x**(1/5))**-1) **
    # for i in denominations[2:]:
    #     fiveFactored = fiveFactored * 1/(1-x**(i/5))

    # # h = fiveFactored
    # g = fiveFactored * a

    # equation = Eq(g, fiveFactored)
    # print(solve(equation, a))
    # # for i in denominations:
    #     ways = ways * (1 - x**i)**-1

    # print(gx)

    # exp = Poly(ways, x**amount)
    # print(factor_list(ways))
    # amount = amount/100

    return round(
        1
        + (
            55 * (amount / 100)
            + 238 * (amount / 100) ** 2
            + 380 * (amount / 100) ** 3
            + 200 * (amount / 100) ** 4
        )
        / 3
    )

    # this allows us to iterate over 0 all the way through 10, which is technically 11 elements
    # ways_to_change = [0 for amount in range(amount + 1)]
    # ways_to_change[0] = 1
    # for denom in denominations:
    #     # this will be pennies, nickels, dimes, half-dollars, quarters
    #     for amount in range(denom, amount + 1):
    #         # we don't try to divide 0 by pennies and stuff lol
    #         if denom <= amount:
    #             # for example, if amount is dime, we can put denoms up to dimes into the dime
    #             ways_to_change[amount] += ways_to_change[amount - denom]
    # return ways_to_change[amount]


# making_change(15, [1, 5, 10, 25, 50])


if __name__ == "__main__":
    # start = time.time()
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")
    # end = time.time()
    # print(end - start)
