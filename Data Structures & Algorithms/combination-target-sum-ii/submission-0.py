class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        candidates.sort()
        def dfs(i, cur_path, total):
            if total == target:
                output.append(sorted(cur_path))
                return
            
            
            # otherwise make a path for each number

            for j in range(i, len(candidates)):
                if candidates[j] + total > target:
                    return

                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                cur_path.append(candidates[j])
                dfs(j + 1, cur_path, candidates[j] + total)
                cur_path.pop()
        dfs(0, [], 0)
        return output

        