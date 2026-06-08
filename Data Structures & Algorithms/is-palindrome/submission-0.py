import re, string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tbl = str.maketrans('','', string.punctuation+' ')
        s = s.translate(tbl).lower()
        return s[::-1]==s
        