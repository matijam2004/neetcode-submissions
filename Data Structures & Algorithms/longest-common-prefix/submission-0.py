class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        shortest = min(strs, key = len)
        out = []
        for i in range(0, len(shortest)):
            ch = shortest[i]
            if all(word[i] == ch for word in strs):
                out.append(ch)
            else:
                break
        return ''.join(out)