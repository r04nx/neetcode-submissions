import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        output = []
        for i, con in enumerate(nums):
            new_lst = nums[:i] + nums[i+1:]
            output.append(math.prod(new_lst))


        return output



        