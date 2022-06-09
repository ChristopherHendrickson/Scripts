#Given a number n, return a list of all valid strings of parenthesis of length n
#A parenthesis string is valid if all opening brackets have a corresponding closing bracket
#and no there are no closing brackets without an associated openin bracket before it
#eg for n=4, ['()()'] is valid. ['())('] is not

def add_open_and_close_bracket(n,possibles_lst=[],lst=[]):
    #Generates all possible combinations of opening and closing brackets of length n
    #a value of 1 represents an open bracket, -1 a closing bracket
    #This works recursively. Each iteration the function makes two new lists from the input by appending a 1 and -1.
    #Then checks if the list is of length n. if it is, it appends it to the output list, otherwise it calls itself again with the new lists
    lst_open = lst[:]
    lst_open.append(-1)
    lst_close = lst[:]
    lst_close.append(1)
    if len(lst_close) == n:
        possibles_lst.append(lst_open)
        possibles_lst.append(lst_close)
    else:
        add_open_and_close_bracket(n,possibles_lst,lst_open)
        add_open_and_close_bracket(n,possibles_lst,lst_close)
    return possibles_lst
    


def valid(lst):
    #returns a list of valid parenthesis strings 
    valid_lst = []
    for bracket_sequence in lst:
        sum = 0
        for value in bracket_sequence:
            sum += value
            if sum < 0: #Means a close bracket occured without a previous open bracket
                break
        if sum == 0: #Means there is an equal amount of open and closing brackets
            for [counter,value] in enumerate(bracket_sequence):
                if value == 1:
                    bracket_sequence[counter]='('
                else:
                    bracket_sequence[counter]=')'
            valid_lst.append(''.join(bracket_sequence))
    return valid_lst


def generateParenthesis(n):
    if n==0:
        return []
    return valid(add_open_and_close_bracket(n*2))

#Written as a Solution class

class Solution:
    def generateParenthesis(self, n):
        if n==0:
            return []
        return self.valid(self.add_open_and_close_bracket(n*2))
    
    def add_open_and_close_bracket(self,n,possibles_lst=[],lst=[]):

        lst_open = lst[:]
        lst_open.append(-1)
        lst_close = lst[:]
        lst_close.append(1)
        if len(lst_close) == n:
            possibles_lst.append(lst_open)
            possibles_lst.append(lst_close)
        else:
            if sum(lst_open)>=0:
                self.add_open_and_close_bracket(n,possibles_lst,lst_open)
            if sum(lst_close)>=0:
                self.add_open_and_close_bracket(n,possibles_lst,lst_close)
        return possibles_lst



    def valid(self,lst):
        #returns a list of valid parenthesis strings 
        valid_lst = []
        for bracket_sequence in lst:
            sum = 0
            for value in bracket_sequence:
                sum += value
                if sum < 0: #Means a close bracket occured without a previous open bracket
                    break
            if sum == 0: #Means there is an equal amount of open and closing brackets
                for [counter,value] in enumerate(bracket_sequence):
                    if value == 1:
                        bracket_sequence[counter]='('
                    else:
                        bracket_sequence[counter]=')'
                valid_lst.append(''.join(bracket_sequence))
        return valid_lst


    
print(Solution().generateParenthesis(1))
