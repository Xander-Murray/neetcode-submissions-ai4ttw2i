class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m_inc, m_dec = 1, 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                m_inc = 1
                m_dec = 1
            elif nums[i - 1] < nums[i]: 
                m_dec = 1
                m_inc += 1
            else:
                m_inc = 1
                m_dec += 1
            res = max(res, m_inc, m_dec)

        return res

        