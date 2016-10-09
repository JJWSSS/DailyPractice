from queue import Queue

try:
    while True:
        max_num = int(input(''))
        num = int(input(''))
        q = Queue(maxsize=max_num)
        l = []
        counter = 0
        for i in range(num):
            x = int(input(''))
            if q.full():
                if x not in l:
                    t = q.get()
                    q.put(x)
                    l.remove(t)
                    l.append(x)
                    counter += 1
            else:
                if x not in l:
                    q.put(x)
                    l.append(x)
                    counter += 1
        print(counter)
except EOFError as e:
    pass
