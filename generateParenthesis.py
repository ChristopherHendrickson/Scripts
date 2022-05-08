


def possibles(n,possibles_lst,lst):
    if len(lst)<=n:
        lst_neg = lst[:]
        lst_neg.append(-1)
        lst_pos = lst[:]
        lst_pos.append(1)
        if len(lst_pos) == n:
            possibles_lst.append(lst_pos)
        if len(lst_neg) == n:
            possibles_lst.append(lst_neg)
        possibles(n,possibles_lst,lst_neg)
        possibles(n,possibles_lst,lst_pos)

    return possibles_lst


def valid(lst):
    
    valid_lst = []
    for i in lst:
        sum_tot = 0
        for value in i:
            sum_tot += value
            if sum_tot < 0:
                break
        if sum_tot == 0:
            for value in enumerate(i):
                if value[1] == 1:
                    i[value[0]]='('
                else:
                    i[value[0]]=')'
            valid_lst.append(''.join(i))
    return valid_lst


def generateParenthesis(n):

    return valid(possibles(n,[],[]))

print(generateParenthesis(4))
