class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        #Merge the two sorted arrays
        sortedNums = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0]<=nums2[0]:
                sortedNums.append(nums1.pop(0))
            else:
                sortedNums.append(nums2.pop(0))
        #Add remaining nums
        sortedNums+=nums1+nums2
        #Find median
        if len(sortedNums)%2 == 0:
            middleLeft = sortedNums[int(len(sortedNums)/2-1)]
            middleRight = sortedNums[int(len(sortedNums)/2)]
            median = (middleLeft+middleRight)/2
        else:
            median = sortedNums[int((len(sortedNums))//2)]
        return median


print(Solution().findMedianSortedArrays([1,2],[3,4]))



