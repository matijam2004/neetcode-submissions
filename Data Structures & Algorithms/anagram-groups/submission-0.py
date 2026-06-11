class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) #defaultdict automatically creates default value
        for w in strs:
            key = "".join(sorted(w))
            dict[key].append(w)
        return list(dict.values())

        
        
