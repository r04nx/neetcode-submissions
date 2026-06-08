class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            current = i
            for j in range(n):
                if target == nums[j] + nums[i] and i!=j:
                    return [i, j]

    
            

        