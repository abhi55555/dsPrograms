def reverse_word(s):
    s = s + ' '
    res = []
    i = 0
    for ch in range(len(s)):
        if s[ch] == ' 'or s[ch] == '\t':
            res.append(s[i:ch])
            i = ch + 1
    for i in range(len(res)):
        print(res.pop(), end=' ')


def reverse_word2(s):
    res = s.split()
    res.reverse()
    res = ' '.join(res)
    print(res)


string = '''i am a disco dancer'''
reverse_word2(string)
