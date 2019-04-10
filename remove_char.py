
def removeChar(string, character):

    counts = string.count(character)

    string = list(string)

    while counts:

        string.remove(character)

        counts -= 1

    string = ''.join(string)

    print(string)


s = "I am a disco dancer"
removeChar(s, 'd')
