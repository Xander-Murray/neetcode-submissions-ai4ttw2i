class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return [key for key, value in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
