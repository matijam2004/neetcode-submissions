class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in range(len(nums)):
            if count == 0:
                candidate = nums[n]
            if candidate == nums[n]:
                count += 1 
            else:
                count -= 1
        return candidate
          