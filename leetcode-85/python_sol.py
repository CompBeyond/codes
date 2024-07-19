class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        acc = [0 for _ in range(m)]
        mx_a = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    acc[j] += 1
                else:
                    acc[j] = 0
            for j in range(m):
                height = 10000000
                for k in range(j, m):
                    height = min(height, acc[k])
                    if height == 0:
                        break
                    width = k - j + 1
                    mx_a = max(mx_a, height * width)
        return mx_a
