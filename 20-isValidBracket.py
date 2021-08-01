# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = [s[0]]
        for char in s[1:]:
            if stack != [] and ((stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')') or (stack[-1] == '[' and char == ']')):
                stack.pop()
            else:
                stack.append(char)
        if stack != []:
            return False
        else:
            return True


print(Solution().isValid("()[{]}"))
