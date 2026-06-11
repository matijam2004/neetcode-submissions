class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            hashset.add(n)

        
        longest = 0
        for n in hashset:
            if n-1 not in hashset:  
                length = 1
                while (n + length) in hashset:
                    length += 1
                longest = max(longest, length)
        return longest   