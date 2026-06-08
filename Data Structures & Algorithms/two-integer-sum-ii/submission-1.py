class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n

        while left<right:
            mysum = numbers[left]+numbers[right-1]
            print(mysum)
            if mysum == target:
                return [left+1, right]

            if mysum > target:
                right-=1
            if mysum < target:
                left+=1
            


        