from typing import List
class Solution:
    def TwoSum(self,nums:List[int],target:int)->List[int]:
        visited = {}
        for i in range(0,len(nums)):
            rem = target-nums[i]
            if rem in visited:
                return [visited[rem],i]
            else:
                visited[nums[i]]=i
        return []
    
    if __name__=="__main__":
        target=9
        number =[2,11,15,7]
        solution=Solution()
        print(solution.TwoSum(number, target))
        