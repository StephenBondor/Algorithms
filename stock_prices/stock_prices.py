#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # find the max profit from the highest number
    maxPrice = max(prices)
    locationOfMax = max(loc for loc, val in enumerate(
        prices) if val == maxPrice)
    if locationOfMax != 0:
        minPriceFromMax = min(prices[0:locationOfMax])
        maxProfitFromMax = maxPrice - minPriceFromMax
    else:
        maxProfitFromMax = max(prices[1:]) - maxPrice

    # find the max profit from the lowest number
    minPrice = min(prices)
    locationOfMin = prices.index(minPrice)
    if locationOfMin != len(prices)-1:
        maxPriceFromMin = max(prices[locationOfMin:])
        maxProfitFromMin = maxPriceFromMin - minPrice
    else:
        maxProfitFromMin = minPrice - min(prices[:-1])

    # return whichever is greater
    if maxProfitFromMin > maxProfitFromMax:
        return maxProfitFromMin
    else:
        return maxProfitFromMax


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
