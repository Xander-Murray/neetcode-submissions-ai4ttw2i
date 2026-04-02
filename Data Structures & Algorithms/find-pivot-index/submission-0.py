class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre[i + 1] = pre[i] + nums[i]

        for i in range(len(nums)):
            if pre[i] == pre[-1] - pre[i + 1]:
                return i
        return -1
        