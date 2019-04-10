# program to remove given character from given string


def removeChar(str, characters):
    table = {}
    temp = []
    for char in characters.lower():
        table[char] = 1

    index = 0
    for char in str.lower():
        if char in table:
            continue
        else:
            temp.append(char)
            index += 1

    return ''.join(temp)


print(removeChar('Airport', 'a'))
