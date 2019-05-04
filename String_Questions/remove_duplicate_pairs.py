# abbabc -> bc ,final string will not have any duplicate pairs

s = 'abbabc'
lists = []
[lists.append(c) for c in s]

i = 1
while(i < len(lists)):
    if lists[i] == lists[i - 1]:
        lists.pop(i)
        lists.pop(i - 1)
        i -= 2
    i += 1

print(''.join(lists))
