def create_cibiao(filename):
    cibiao = {}
    with open(filename, 'rt', encoding='utf8') as f:
        for word in iter(lambda: next(f, None), None):
            if not word.startswith('1998'):
                cibiao[word.strip()] = True
    return cibiao


def reverse_pipei(f, cibiao, sentence, max_length=5):
    sentence = sentence.rstrip()
    l = []
    single_word = 0
    end = len(sentence) - 1
    while end >= 0:
        for i in range(max_length, 0, -1):
            if i == 1:
                l.append(sentence[end])
                end -= i
                single_word += 1
                break
            else:
                start = end - i + 1
                if start < 0:
                    start = 0
                if cibiao.get(sentence[start: end+1]):
                    l.append(sentence[start: end+1])
                    end -= i
                    break
    for i in l[::-1]:
        f.write(i)
        f.write('  ')
    f.write('\n')


if __name__ == '__main__':
    cibiao = create_cibiao('cibiao.utf8')
    with open('fenci.txt', 'wt', encoding='utf8') as f:
        with open('yuliao.utf8', 'rt', encoding='utf8') as f1:
            for s in iter(lambda: next(f1, None), None):
                reverse_pipei(f, cibiao, s)
    with open('fenci.txt', 'rt', encoding='utf8') as f:
        with open('gold_yuliao.utf8', 'rt', encoding='utf8') as f1:
            number = 0
            right = 0
            while True:
                l1 = next(f, None)
                l2 = next(f1, None)
                if l1 is None or l2 is None:
                    break
                if l1 == l2:
                    right += 1
                number += 1
            print(right/number)



