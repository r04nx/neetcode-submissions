class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        n = len(nums)
        nums = set(nums)
        for i in nums:
            if i-1  in nums:
                continue
            count = 1
            start = i
            while start+1 in nums:
                count+=1
                start+=1
            max_count = max(max_count, count)

        return max_count


        
        