class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_to_let = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


        res = []
        path = []

        def dfs(idx: int):
            
            if idx >= len(digits):
                res.append("".join(path))
                return

            
            for let in num_to_let[digits[idx]]:
                path.append(let)
                dfs(idx + 1)
                path.pop()
        dfs(0)
        return res
            


            
        