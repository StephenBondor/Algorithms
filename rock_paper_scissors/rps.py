#!/usr/bin/python

import sys


# def h(l, n):
#     return (
#         [l]
#         if n == 0
#         else h(l + ["rock"], n - 1)
#         + h(l + ["paper"], n - 1)
#         + h(l + ["scissors"], n - 1)
#     )


# def h(n, l, p=["rock", "paper", "scissors"]):
#     return [l] if n == 0 else sum([h(n - 1, l + [p[i]]) for i in range(3)], [])


def rps(n, l=[], p=["rock", "paper", "scissors"]):
    return [l] if n == 0 else sum([rps(n - 1, l + [p[i]]) for i in range(3)], [])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rps(num_plays))
    else:

        print("Usage: rps.py [num_plays]")


# in JS

# function rockPaperScissors(num) {
#   let arr = []

#   function helper(arr, num){
#     // console.log("interation: ", num, " array: ", arr)
#     if (num == 0){
#       return [arr];
#     }
#     return [...helper([...arr, "rock"], num-1),
#             ...helper([...arr, "paper"], num-1),
#             ...helper([...arr, "scissors"], num-1)]
#   }
#   if (num == 0){
#     return [[]]
#   }
#   return helper([], num)
# }

# /* Some console.log tests */
# const rv0 = rockPaperScissors(0);
# console.log(rv0);

# const rv1 = rockPaperScissors(1);
# console.log(rv1);

# const rv22 = rockPaperScissors(2);
# console.log(rv22);   // should print [[rock, rock], [rock, paper], [rock, scissors], [paper, rock], [paper, paper], [paper, scissors], [scissors, rock], [scissors, paper], [scissors, scissors]]

# const rv2 = rockPaperScissors(3);
# console.log(rv2);    // should print 27

# const rv3 = rockPaperScissors(4);
# console.log(rv3.length);    // should print 81

# const rv4 = rockPaperScissors(5);
# console.log(rv4.length);    // should print 243
