class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for _ in range(n+1)] for _ in range(m+1)]
        mat[m-1][n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r== m-1 and c == n-1:
                    continue
                mat[r][c] = mat[r+1][c] + mat[r][c+1]

        return mat[0][0]

        