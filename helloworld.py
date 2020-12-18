

x = [1, 2]
y = [3, 4]

print(list(e for e in x or y))

print(str(bin(5))[2:])

from itertools import permutations
from itertools import combinations

x = [1, 2, 3, 4, 5]

print(list(permutations(x)))  # 全排列
print(list(permutations(x, 2)))  # 部分排列
print(list(combinations(x, 2)))  # 组合


