# #Given a number n, return a list of all valid strings of parenthesis of length n
# #A parenthesis string is valid if all opening brackets have a corresponding closing bracket
# #and no there are no closing brackets without an associated opening bracket before it
# #eg for n=2, ['()()'] is valid. ['())('] is not
class Solution:
    def runner(self, n, seq, add, output, sum):
        valid=True
        seq+=add
        
        if seq[-1] == "(":
            sum+=1
            if sum>n/2:
                valid=False
                
        else:
            sum-=1
            if sum < 0:
                valid=False
                
        if len(seq)==n and valid and sum == 0:
            output.append(seq)
            
        if valid and len(seq)<n:
            self.runner(n,seq,"(",output,sum)
            self.runner(n,seq,")",output,sum)
        
        return output
    
    def generateParenthesis(self, n): #Had to separate the fucntions so the output list would reset over diffrerent function calls. Dont fully understand why it was necessary..
        return self.runner(n*2, "", "(", [], 0)
        
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))