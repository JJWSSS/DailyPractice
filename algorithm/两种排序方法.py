n = input('')
s = ''
length = True
dicc = True
for i in range(int(n)):
    if i == 0:
        s = input('')
    else:
        s1 = input('')
        if s > s1:
            dicc = False
        if len(s) > len(s1):
            length = False
        s = s1
if length and dicc:
    print('both')
elif length:
    print('lengths')
elif dicc:
    print('lexicographically')
else:
    print('none')
