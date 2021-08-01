# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
class Solution:

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False for i in range(l)] for j in range(l)]  # dp[i][j]表示s[i:j+1]是不是回文字串
        for i in range(l):
            dp[i][i] = True
        max_len = 1
        max_start = 0
        max_end = 0
        for end in range(1, l):
            for start in range(end):
                if (s[start] == s[end] and (start == end - 1 or dp[start + 1][end - 1])):
                    dp[start][end] = True
                    cur_l = end - start + 1
                    if cur_l > max_len:
                        max_start = start
                        max_end = end
                        max_len = cur_l
                else:
                    dp[start][end] = False
        return s[max_start:max_end + 1]


print(Solution().longestPalindrome("babaddtattarrattatddetartrateedredividerb"))