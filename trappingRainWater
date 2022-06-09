# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
class Solution:
    def trap(self, height):
        left=0
        right=len(height)-1
        boundaryHeight=min(height[left],height[right])
        sum=boundaryHeight*(right-left)
        while left!=right:
            if height[left]>height[right]:
                sum-=min(boundaryHeight,height[right])
                right-=1
            else:
                sum-=min(boundaryHeight,height[left])
                left+=1
            
            nextBoundaryHeight=min(height[left],height[right])
            if nextBoundaryHeight > boundaryHeight:
                sum+=(right-left)*(nextBoundaryHeight-boundaryHeight)
                boundaryHeight=nextBoundaryHeight
        return sum

print(Solution().trap([4,2,0,3,2,5]))
