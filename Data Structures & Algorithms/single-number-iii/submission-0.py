class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res, n = [], len(nums)
        nums.sort()

        for i in range(n):
            if ((i > 0 and nums[i] == nums[i - 1]) or 
                (i + 1 < n and nums[i] == nums[i + 1])):
                continue
            res.append(nums[i])
        return res