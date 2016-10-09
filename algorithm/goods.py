from collections import defaultdict

while True:
    s = input('')
    if s == '':
        break
    price_num = int(s.split(' ')[0])
    goods_num = int(s.split(' ')[1])
    price_min = sorted(map(int, input('').split(' ')))
    price_max = price_min[::-1]
    goods = defaultdict(int)
    for i in range(goods_num):
        s = input('')
        goods[s] += 1
    goods_number = sorted(goods.values(), reverse=True)
    min_price = 0
    max_price = 0
    for i in range(len(goods_number)):
        min_price += goods_number[i] * price_min[i]
        max_price += goods_number[i] * price_max[i]
    print(min_price, max_price)

