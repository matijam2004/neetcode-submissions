class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2): #how many times I want to run a loop
            for n in nums: #for each number in nums array
                ans.append(n) # add that number to ans array (append)
        return ans #return the answer




        