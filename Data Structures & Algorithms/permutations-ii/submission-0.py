class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # put duplicates next to each other
        res = []
        used = [False] * len(nums) # tracks which indeices are already in the current lst

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                path.append(nums[i])

                backtrack(path)
                
                path.pop()
                used[i] = False
        backtrack([])
        return res