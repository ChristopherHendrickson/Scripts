class Solution(object):
    def romanToInt(self, s):
        conversion = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        sum = 0 
        for i in range(len(s)-1):
            numeral = s[i]
            numeral_next = s[i+1]
            if conversion[numeral]<conversion[numeral_next]:
                sum-= conversion[numeral]
            else:
                sum+=conversion[numeral]
        sum+=conversion[s[-1]]
        return sum

print(Solution().romanToInt('IV'))