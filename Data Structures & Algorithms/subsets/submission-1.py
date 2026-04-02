class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        


        subset = []
        # i is index of number in nums
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

                # decision to include nums[i]
                # left branch
            subset.append(nums[i])
            dfs(i + 1)

                # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res






        
        
        

        # Always need an empty set

        # what is a sub set?
        # [], each num by its self, and every combinations
        # of numbers (without duplicates) !!NOT A PERMUTATION!
        # 2^n is the number of subsets
        # worst case is (n x 2^n)

        # draw a decision tree will usuall help

        

        