class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        while left<right:
            mysum = numbers[left]+numbers[right]
            print(mysum)
            if mysum == target:
                return [left+1, right+1]

            if mysum > target:
                right-=1
            elif mysum < target:
                left+=1
            


        