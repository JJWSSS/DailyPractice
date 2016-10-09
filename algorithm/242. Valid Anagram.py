from collections import Counter


def is_anagram(s, t):
    a = Counter(s)
    b = Counter(t)
    return True if a == b else False

if __name__ == '__main__':
    print(is_anagram('aa', 'a'))
