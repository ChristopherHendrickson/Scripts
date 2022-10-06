class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_reverse = s[::-1]
        max=0
        out=''
        for i in range(len(s)):
            
            for j in range(1,len(s)-i+1):
                if s[i:i+j] in s_reverse:
                    #Check if palindrome is longer than previous longest,
                    #and check if palindrome ends at the correct start point of the reversed string
                    if j>max and i+j == len(s)-s_reverse.find(s[i:i+j]):
                        max = j
                        out = s[i:i+j]
                else:
                    break
            if max > len(s)/2:
                break
        return out

print(Solution().longestPalindrome("ccccccccccccacc"))

