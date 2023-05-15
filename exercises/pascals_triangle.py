# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows):
        rows = []
        for n in range(1, numRows + 1):
            if n < 3:
                rows.append(n * [1])
            else:
                above_row = rows[-1]
                row = []
                for i in range(1, n + 1):
                    if i == 1 or i == n:
                        row.append(1)
                    else:
                        index = len(row)
                        row.append(above_row[index - 1] + above_row[index])
                rows.append(row)

        return rows
        