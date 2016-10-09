s_a = input('')
s_b = input('')
number = 0
for i in range(-1, len(s_a)):
    if i == -1:
        s = ''.join((s_b, s_a))
        if s[:] == s[::-1]:
            number += 1
    else:
        s = ''.join((s_a[0:i+1], s_b, s_a[i+1:]))
        if s[:] == s[::-1]:
            number += 1
print(number)
