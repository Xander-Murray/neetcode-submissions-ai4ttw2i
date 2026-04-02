class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j]> target:
                    # no need to go down this path
                    return
                #otherwise add next num to the path and recurse with taht number now in the path
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                # we pop so we can have another 'path' with the next number in nums
                '''
                [2, 2]
                /          \
            [2,2,3]         [2,2]
            /     \             /    \
        [2,2,3,6][2,2,3]   [2,2,6]     [2,2]
                '''
                path.pop()
        dfs(0, [], 0)
        return res


        