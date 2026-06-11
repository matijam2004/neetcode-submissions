class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        TChar = {}
        for i in s:
            chars[i] = chars.get(i, 0) + 1
        
        for i in t:
            TChar[i] = TChar.get(i, 0) + 1
        
        if chars == TChar:
            if len(s) == len(t):
                return True
        return False