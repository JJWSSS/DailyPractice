while True:
    s = input('')
    if not s:
        break
    time = int(s.split(' ')[0])
    length = int(s.split(' ')[1])
    jubing = 1
    weifenpei = [[1, length]]
    yifenpei = []
    for i in range(time):
        x = input('')
        y = x.split(' ')
        if y[0] == 'del':
            for t, j, k in yifenpei:
                if t == int(y[1]):
                    yifenpei.remove([t, j, k])
                    for w, v in weifenpei:
                        if w == k+1:
                            weifenpei[weifenpei.index([w, v])][0] = j
                            break
                        if v == j-1:
                            weifenpei[weifenpei.index([w, v])][1] = k
                            break
                    else:
                        weifenpei.append([j, k])
                    break
            else:
                print('ILLEGAL_OPERATION')
        elif y[0] == 'new':
            weifenpei = sorted(weifenpei)
            for w, v in weifenpei:
                if v-w+1 > int(y[1]):
                    yifenpei.append([jubing, w, w+int(y[1])-1])
                    weifenpei[weifenpei.index([w, v])][0] = w+int(y[1])
                    print(jubing)
                    jubing += 1
                    break
                if v-w+1 == int(y[1]):
                    yifenpei.append([jubing, w, v])
                    weifenpei.remove([w, v])
                    print(jubing)
                    jubing += 1
                    break
            else:
                print('NULL')
        else:
            yifenpei = sorted(yifenpei, key=lambda l: l[1])
            j = 1
            for t in range(len(yifenpei)):
                q = yifenpei[t][2] - yifenpei[t][1]
                yifenpei[t][1] = j
                yifenpei[t][2] = j+q
                j += q+1
            weifenpei = [[j, length]]

