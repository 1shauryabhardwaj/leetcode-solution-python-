class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb_nums = []
        # 1. Fist combine two array
        # 2. Sort it: Can be Insertion sort, quick sort, shell sort, hybrid sort
        # 3. Find median
        
        # 1.
        comb_nums = nums1 + nums2
        # 2.
        if len(comb_nums) ==0:
            return 0
        elif len(comb_nums)==1:
            return comb_nums[0]
        
        if len(nums1) !=0 or len(nums2) !=0:
            comb_nums.sort()
        # 3.
        return self.findMedian(comb_nums)
        
        
    def findMedian(self, lst):
        lstlen = len(lst)
        index = (lstlen -1)//2
        if(lstlen % 2): # odd length
            return lst[index]
        else: # even length
            return (lst[index] + lst[index + 1])/2.0