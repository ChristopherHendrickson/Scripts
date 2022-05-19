#Given a number n, return a list of all valid strings of parenthesis of length n
#A parenthesis string is valid if all opening brackets have a corresponding closing bracket
#and no there are no closing brackets without an associated openin bracket before it
#eg for n=4, ['()()'] is valid. ['())('] is not

def possibles(n,possibles_lst=[],lst=[]):
    #Generates all possible combinations of opening and closing brackets of length n
    #a value of 1 represents an open bracket, -1 a closing bracket
    #This works recursively. Each iteration the function makes two new lists from the input by appending a 1 and -1.
    #Then checks if the list is of length n. if it is, it appends it to the output list, otherwise it calls itself again with the new lists
    lst_neg = lst[:]
    lst_neg.append(-1)
    lst_pos = lst[:]
    lst_pos.append(1)
    if len(lst_pos) == n:
        possibles_lst.append(lst_neg)
        possibles_lst.append(lst_pos)
    else:
        possibles(n,possibles_lst,lst_neg)
        possibles(n,possibles_lst,lst_pos)
    return possibles_lst
    


def valid(lst):
    #returns a list of valid parenthesis strings 
    valid_lst = []
    for i in lst:
        sum_tot = 0
        for value in i:
            sum_tot += value
            if sum_tot < 0: #Means a close bracket occured without a previous open bracket
                break
        if sum_tot == 0:
            for [counter,value] in enumerate(i):
                if value == 1:
                    i[counter]='('
                else:
                    i[counter]=')'
            valid_lst.append(''.join(i))
    return valid_lst


def generateParenthesis(n):
    return valid(possibles(n))



#print(generateParenthesis(6))
print(possibles(4))
