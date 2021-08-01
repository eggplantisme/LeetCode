# 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。

# 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
import time
class Solution:

    def canWinNim(self, n: int) -> bool:
        # pre_1 = True
        # pre_2 = True
        # pre_3 = True
        # pre_4 = False
        # for i in range(4, n + 1):
        #     pre_4 = (not (pre_1 and pre_2 and pre_3))
        #     pre_1 = pre_2
        #     pre_2 = pre_3
        #     pre_3 = pre_4
        # return pre_4
        return False if n % 4 == 0 else True

print(Solution().canWinNim(1348820612))