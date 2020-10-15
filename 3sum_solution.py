#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:     
        n = len(nums)
        if n < 3: return []  
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = set()
        for i in range(n-2):
            left = i+1
            right = n - 1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    triplet = (nums[i],nums[left],nums[right])
                    if triplet not in result: result.add(triplet)
                    left += 1
                    right -= 1
                elif total > 0: right -= 1
                elif total < 0: left += 1
                    
        return result
            
