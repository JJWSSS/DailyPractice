while True:
    s1 = input('')
    if s1 == '':
        break
    s2 = input('')
    ss = list(map(int, s1))
    ss = sorted(ss)
    for i in range(len(ss)):
        if ss[i] != 0:
            ss[0], ss[i] = ss[i], ss[0]
            break
    if list(map(int, s2)) == ss:
        print('YES')
    else:
        print('NO')
