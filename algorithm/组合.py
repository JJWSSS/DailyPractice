from itertools import combinations
from operator import mul
from functools import reduce

s = input('')
ss = list(map(int, s.split(' ')))
m = int(input(''))
max_num = -1
for i in range(1, len(ss)+1):
    l = list(combinations(ss, i))
    for j in l:
        if sum(j) == m:
            t = reduce(mul, j)
            if t > max_num:
                print(j, t)
                max_num = t
print(max_num)
