try:
    while True:
        num = int(input(''))
        numbers = list(map(int, input('').split(' ')))
        counter = 1
        for i in range(num-1):
            for j in range(i+1, num):
                if j-i == 1:
                    counter += 1
                elif min(numbers[i], numbers[j]) > max(numbers[i+1:j]):
                    counter += 1
                elif (i != 0 or j != num-1) and min(numbers[i], numbers[j]) > max(numbers[j+1:] + numbers[:i]):
                    counter += 1
        print(counter)
except EOFError as e:
    pass
