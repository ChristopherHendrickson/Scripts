#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this
# P   A   H   N
# A P L S I I G
# Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#This code makes this conversion given a number of rows deep that the zigzag goes (The example above was 3)
class Solution:
    def convert(self, str, numRows):
        
        output=''
        if numRows==1:
            row_steps=[1]
        else:
            row_steps = [2*n-2 for n in range(numRows,1,-1)]
            row_steps.append(row_steps[0])
        row_steps.insert(0,0)
        print(row_steps)
        for i in range(1,numRows+1):
            index = i-1
            switch=1
            while index < len(str):
                output+=(str[index])
                index+=row_steps[i*switch]
                if switch == -1: switch = 1
                else: switch = -1
                
        return output
print(Solution().convert('A',1))