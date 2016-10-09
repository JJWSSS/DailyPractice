while True:
    x = input('')
    if x == '':
        break
    x = int(x)
    if x == 0:
        print(0)
    else:
        if x < 0:
            x = -x
        step = 1
        times = 0
        while x >= step:
            times += 1
            x -= step
            step += 1
        times += x*2
        print(times)
