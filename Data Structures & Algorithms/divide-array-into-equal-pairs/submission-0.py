class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        pairs = 0
        for k, v in cnt.items():
            if v % 2 != 0:
                return False
            pairs += v / 2

        return True if pairs == len(nums) / 2 else False