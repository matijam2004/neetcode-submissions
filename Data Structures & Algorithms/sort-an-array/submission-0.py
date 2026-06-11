class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            left = nums[:len(nums)//2]
            right = nums[len(nums)//2:]

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            # while both halves still have elements
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # one half is exhausted, append whatever is left
            result.extend(left[i:])
            result.extend(right[j:])
            return result
            
        return mergeSort(nums)