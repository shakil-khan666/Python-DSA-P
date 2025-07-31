from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_maps={}
        for num in nums:
            if num not in count_maps:
                count_maps[num] = 1
            else:
                count_maps[num]=count_maps[num]+1
                
        for num,count in count_maps.items():
            if count>len(nums)/2:
                return num
                
            
number = [2,2,3,4,4,4,4]
s = Solution()

print(s.majorityElement(number))