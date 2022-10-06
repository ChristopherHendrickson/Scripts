class Solution:
    def longestValidParentheses(self, s):
        if s == '':
            return 0
        forwardLongest = self.checkParentheses(s,'(')
        reverseLongest = self.checkParentheses(s[::-1],')')
        return max(forwardLongest,reverseLongest)
        
    def checkParentheses(self,s,bracketDir):
        longest = 0
        sum=0
        startingIndex=0

        for n in range(len(s)):
            if s[n] == bracketDir:
                sum+=1
            else:
                sum-=1
                if sum < 0:
                    startingIndex=n+1
                    sum=0    
                if sum == 0 and n-startingIndex+1 > longest:
                    longest = n-startingIndex+1
                
        return longest


testCase = "))))()(((()))())"

print(Solution().longestValidParentheses(testCase))