# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution:
    def maxArea(self, height):
        n=len(height)
        left = 0
        right = n-1
        maxArea=0
        while right!=left:
            area=min(height[left],height[right])*(right-left)
            if area>maxArea:
                maxArea=area
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1

        return maxArea

test = [1,2,4,3]
print(Solution().maxArea(test))