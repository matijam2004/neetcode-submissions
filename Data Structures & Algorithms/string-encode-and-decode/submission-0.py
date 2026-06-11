class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for n in strs:
            string += str(len(n)) + '#' + n
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        length = 0
        string = ""
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strings.append(s[j+1 : j+1+length])
            i = j+1+length
        return strings