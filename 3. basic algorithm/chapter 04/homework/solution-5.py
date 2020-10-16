# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    绘制排列函数PuzzleSolve(3, S, U)的递归跟踪, S为空, U为{'a', 'b', 'c', 'd'}
"""

from helloutils.tracker import Track

res = []

@Track
def puzzle_solve(k, s:list, u:set):
    if k == 0:
        res.append(s.copy())

    else:
        for each in u.copy():
            u.remove(each)
            s.append(each)
            puzzle_solve(k - 1, s, u)

            s.remove(each)
            u.add(each)


puzzle_solve(3, [], {'a', 'b', 'c'})
print(res)