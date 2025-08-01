from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=nums.sort()
        x = len(nums)
        mid=int(x/2)
        return nums[mid]
        
        
number = [2,2,3,4,4,4,4]
s = Solution()
print(s.majorityElement(number))