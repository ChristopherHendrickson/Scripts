# #Given a number n, return a list of all valid strings of parenthesis of length n
# #A parenthesis string is valid if all opening brackets have a corresponding closing bracket
# #and no there are no closing brackets without an associated openin bracket before it
# #eg for n=4, ['()()'] is valid. ['())('] is not
class Solution:
    def runner(self, n, seq, add, output):
        sum=0
        valid=True
        seq+=add
        for i in range(len(seq)):
            if seq[i] == "(":
                sum+=1
                if sum>n/2:
                    valid=False
                    break
            else:
                sum-=1
                if sum < 0:
                    valid=False
                    break
        if len(seq)==n and valid and sum == 0:
            output.append(seq)
            
        if valid and len(seq)<n:
            self.runner(n,seq,"(",output)
            self.runner(n,seq,")",output)
        
        return output
    
    def generateParenthesis(self, n): #Had to separate the fucntions so the output list would reset over diffrerent function calls. Dont fully understand why it was necessary..
        return self.runner(n*2, "", "(", [])
        
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(2))
# print(Solution().generateParenthesis(2))
