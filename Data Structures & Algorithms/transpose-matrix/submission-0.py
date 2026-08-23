class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])

        if R == C:
            for r in range(R):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

            return matrix

        res = [[0] * R for _ in range(C)]

        for r in range(R):
            for c in range(C):
                res[c][r] = matrix[r][c]
        return res
        