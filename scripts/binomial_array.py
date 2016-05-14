def print_list(l, n):
    s = ''
    for i in l:
        s += str(i)
        s += ' '
    s.rstrip()
    n += n-1
    print(s.center(n))

if __name__ == '__main__':
    number = input('请输入数字:')
    number = int(number)
    l = [1]
    print_list(l, number)
    if number > 1:
        l.append(1)
        print_list(l, number)
        if number > 2:
            for i in range(3, number+1):
                new_l = [1]
                for n in range(i-2):
                    new_l.append(l[n] + l[n+1])
                new_l.append(1)
                print_list(new_l, number)
                l = new_l





