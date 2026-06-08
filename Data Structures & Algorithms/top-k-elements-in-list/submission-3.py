from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dedict = defaultdict(int)

        for i in range(n):
            dedict[nums[i]]+=1


            # if len(dedict)>=k:
            #     break

        result = list(sorted(dedict.items(), key=lambda x:x[1], reverse=True))
        return [i[0] for i in result[:k]]
