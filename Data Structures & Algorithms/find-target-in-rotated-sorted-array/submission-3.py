class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                # check left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                    # target is in between the left and mid bouns
                else:
                    l = m + 1 # target is past right
            else:
                # right side is sorted 
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
                
        return -1
        