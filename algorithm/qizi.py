while True:
    a = input('')
    if not a:
         break
    b = input('')
    c = input('')
    print(a, b, c)
    zheng1 = 1
    x = a.find(b)
    if x != -1:
        y = a.find(c, x+len(b))
        if y != -1:
            zheng1 = 1
        else:
            zheng1 = 0
    else:
        zheng1 = 0
    zheng2 = 1
    t = ''.join(list(a)[::-1])
    x = t.find(b)
    if x != -1:
        y = t.find(c, x + len(b))
        if y != -1:
            zheng2 = 1
        else:
            zheng2 = 0
    else:
        zheng2 = 0
    if zheng1 and zheng2:
        print('both')
    elif zheng1:
        print('forward')
    elif zheng2:
        print('backward')
    else:
        print('invalid')
