# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if x < 0:
            revers_x = int("-" + str_x[1:][::-1])
            if revers_x < - 2 ** 31:
                return 0
            else:
                return revers_x
        else:
            revers_x = int(str_x[::-1])
            if revers_x > 2 ** 31 - 1:
                return 0
            else:
                return revers_x

print(Solution().reverse(1534236469))