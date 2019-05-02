
def k_non_rep_char(st, k):

    table = {}
    count = 1
    for s in st:
        if s in table:
            table[s] += 1
        else:
            table[s] = 1
    for t in table:
        if table[t] == 1:
            if count == k:
                print(t)
                count += 1
            else:
                count += 1


st = 'adokandsvoirnoahbnaosbhnonobns'
k = 3

k_non_rep_char(st, k)
