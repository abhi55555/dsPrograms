def count_substring(string, sub_string):
    count = 0
    n = len(string)
    x = len(sub_string)
    for i in range(n - x + 1):
        if string[i:i + x] == sub_string:
            count += 1

    print(count)


string = 'qwertyertty'
sub_string = 'ty'
count_substring(string, sub_string)
