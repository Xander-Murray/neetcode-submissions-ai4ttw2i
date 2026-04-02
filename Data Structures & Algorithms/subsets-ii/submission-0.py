class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []


        nums.sort()
        def dfs(i, cur_path):
            output.append(cur_path.copy())
                
            
            
            # otherwise make a path for each number

            for j in range(i, len(nums)):
              
                # only skip new paths starting at the same number, we horizontally skip
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                cur_path.append(nums[j])
                dfs(j + 1, cur_path)
                cur_path.pop()
        dfs(0, [])
        return output

        
'''

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
        '''