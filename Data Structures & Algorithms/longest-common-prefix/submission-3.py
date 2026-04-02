class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        pre = ""

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                continue
            else:
                return strs[0][:i]
        return strs[0]