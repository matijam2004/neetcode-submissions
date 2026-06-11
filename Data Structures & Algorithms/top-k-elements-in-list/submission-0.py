class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         my_map = {}

         for n in nums:
            if n not in my_map:
                 my_map[n] = 0
            my_map[n] += 1

         sorted_map = sorted(my_map, key=lambda x: my_map[x], reverse=True)
         return sorted_map[:k]
       