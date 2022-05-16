class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row, col = len(word1) + 1, len(word2) + 1
        tb = [[-1] * (col) for x in range(0, row)]
        for i in range(0, row):
            for j in range(0, col):
                if j == 0:
                    tb[i][j] = i
                elif i == 0:
                    tb[i][j] = j
                elif word1[i - 1] == word2[j - 1]:
                    tb[i][j] = tb[i - 1][j - 1]
                else:
                    tb[i][j] = min(tb[i - 1][j - 1], tb[i - 1][j], tb[i][j - 1]) + 1
        return tb[row - 1][col - 1]