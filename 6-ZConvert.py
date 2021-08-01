# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == "":
            return ""
        row_num = numRows
        if row_num == 1:
            return s
        col_num = (len(s) // (numRows + numRows - 2) + 1) * (numRows - 2 + 1)
        data = [[None for i in range(col_num)] for j in range(row_num)]
        down = True
        right_up = False
        i = -1
        j = 0
        for char in s:
            if down and i + 1 < row_num:
                data[i + 1][j] = char
                i += 1
            elif down:
                down = False
                data[i - 1][j + 1] = char
                right_up = True
                i -= 1
                j += 1
            elif right_up and i - 1 >= 0:
                data[i - 1][j + 1] = char
                i -= 1
                j += 1
            else:
                down = True
                data[i + 1][j] = char
                right_up = False
                i += 1
        result = ""
        for i in range(row_num):
            for j in range(col_num):
                if data[i][j] is not None:
                    result += data[i][j]
        return result

print(Solution().convert("LEETCODEISHIRING", 3))