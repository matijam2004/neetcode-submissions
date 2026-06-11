class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = m = 0
        h = len(nums) - 1
        while m <= h:
            #we compare 0,0 to h which is position 2, after we find that we swap
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                m+=1
                l+=1
            elif nums[m] == 1:
                m+=1
            elif nums[m] == 2:
                nums[h], nums[m] = nums[m], nums[h]
                h-=1

            

        