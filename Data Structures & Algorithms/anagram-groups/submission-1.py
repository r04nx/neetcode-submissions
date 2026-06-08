from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        n = len(strs)
        for i in range(n):
            current_counter = Counter(strs[i])
            current_group = [strs[i]]
            for j in range(n):
                if current_counter == Counter(strs[j]) and i!=j:
                    current_group.append(strs[j])

            if sorted(current_group) not in result:
                print(sorted(current_group))
                result.append(sorted(current_group))

        return result

        