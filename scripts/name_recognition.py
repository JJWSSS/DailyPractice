def create_dic(filename):
    dic = {}
    with open(filename, 'rt', encoding='utf8') as f:
        for x in iter(lambda: next(f, None), None):
            dic[x.strip()] = True
    return dic


def name_recognition(last_name, in_filename, out_filename):
    with open(in_filename, 'rt', encoding='utf8') as f:
        f1 = open(out_filename, 'wt', encoding='utf8')
        for sentence in iter(lambda: next(f, None), None):
            words = sentence.split('  ')
            state = 0
            word_list = []
            for word in words:
                if len(word) == 2 or len(word) == 1:
                    if state == 0:
                        if len(word) == 2 and last_name.get(word):
                            word_list.append(word)
                            state = 1
                        if len(word) == 1 and '\u4e00' <= word <= '\u9fa5' and last_name.get(word):
                            word_list.append(word)
                            state = 1
                    else:
                        if len(word) == 2:
                            word_list.append(word)
                            for i in word_list:
                                f1.write(i)
                                f1.write('  ')
                            f1.write('------  ')
                            f1.write(''.join(word_list))
                            f1.write('\n')
                        word_list.clear()
                        state = 0
        f1.close()


if __name__ == '__main__':
    last_name = create_dic('last.txt')
    name_recognition(last_name, 'fenci.txt', 'name.txt')




