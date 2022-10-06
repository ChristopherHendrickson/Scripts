#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x):
        max="2147483647"
        min="2147483648"
        negative = False
        x=str(x)
        reversed=x[::-1]
        
        #remove the negative sign an take note to add it back later
        if reversed[-1]=="-":
            negative = True
            reversed=reversed[0:len(reversed)-1]

        #check if any index of the string is greater than the 32-bit max/min. If it is less than, stop checking becuase the value is ok
        if len(reversed) == 10:

            for i in range(10):
                print(reversed[i])
                print(max[i])
                if not negative and reversed[i]>=max[i]:
                    if reversed[i]>max[i]:
                        return 0
                elif not negative:
                    break
                
                if negative and reversed[i]>=min[i]:
                    if reversed[i]>min[i]:
                        return 0
                elif negative:
                    break
        
        #Count any preceeding 0's from the output to remove
        firstNonZero=0
        for i in range(len(reversed)):
            if reversed[i]=='0' and not len(reversed) == 1:
                firstNonZero+=1                
            else:
                break
        
        if negative:
            return int("-"+reversed[firstNonZero:])
        return int(reversed[firstNonZero:])


input = 1563847412
print(Solution().reverse(input))