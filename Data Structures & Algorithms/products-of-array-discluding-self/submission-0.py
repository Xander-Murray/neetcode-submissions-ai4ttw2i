class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. Calculate Prefix (Left) products
        # Store them directly in result array
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
            
        # 2. Calculate Suffix (Right) products
        # Multiply them into the result array on the fly
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res