from collections import Counter
from math import log2

if __name__ == '__main__':

    tj = Counter()
    total_number = 0

    with open('199801人民日报.txt', encoding='gbk') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            for zi in line:
                if '\u4e00' <= zi <= '\u9fa5':
                    total_number += 1
                    tj[zi] += 1

    print(total_number)

    print(len(tj))
    print(tj.most_common(100))

    l = [1, 20, 100, 600, 2000, 3000, 6000]

    for n in l:
        print('{} {:0.2f}'.format(n, sum([c[1] for c in tj.most_common(n)])/total_number))

    H = 0

    for _, number in tj.items():
        frequency = number/total_number
        H += frequency*log2(frequency)

    H = -H
    print(H)




