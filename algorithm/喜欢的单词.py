s = input('')
if s.isupper():
    t = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            break
    else:
        t = True
    if t:
        s_d = {}
        for i in range(len(s)):
            if s[i] in s_d.keys():
                s_d[s[i]].append(i)
            else:
                s_d[s[i]] = [i]
        for k, v in s_d.items():
            if len(v) >= 4:
                print('Dislikes')
                break
            w = False
            for i in range(1, len(v)):
                if set(s[v[0]+1:v[i]]) & set(s[v[i]+1:]):
                    break
            else:
                w = True
            if not w:
                print('Dislikes')
                break
        else:
            print('Likes')
    else:
        print('Dislikes')
else:
    print('Dislikes')
