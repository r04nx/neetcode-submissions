class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        result = ""
        n = len(strs)
        for i in range(n):
            result+=str(len(strs[i]))+"#"+strs[i]
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        result = []
        
        j = 0
        idx = 0
        while idx < len(s):
            currl = 0
            currs = ""
            j = idx
            while s[j]!="#":
                j+=1
            
            currl = int(s[idx:j])

            print(currl)

            currs = s[j+1:j+1+currl]
            result.append(currs)
            idx = j+1+currl
            print(result)
        return result
        


# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         result = ""
#         for s in strs:
#             result += str(len(s)) + "#" + s
#         return result

#     def decode(self, s: str) -> List[str]:
#         if s == "":
#             return []
        
#         result = []
#         idx = 0
        
#         while idx < len(s):
#             # find the #
#             j = idx
#             while s[j] != "#":
#                 j += 1
            
#             length = int(s[idx:j])  # number before #
#             start = j + 1           # starting index of string
#             end = start + length    # ending index
            
#             result.append(s[start:end])
            
#             idx = end  # move to next encoded block
        
#         return result


