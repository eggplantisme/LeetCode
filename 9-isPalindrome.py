# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.isPalindromeStr(str(x))

    def isPalindromeStr(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        else:
            if s[0] == s[-1]:
                return self.isPalindromeStr(s[1:-1])
            else:
                return False
    