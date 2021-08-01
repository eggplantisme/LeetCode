class Solution:
    def intToRoman(self, num: int) -> str:
        # num 1~3999
        str_num = str(num)
        result = ""
        for i in range(len(str_num)):
            decimal_bit = len(str_num) - i
            n = int(str_num[i])
            if decimal_bit == 4:
                result += "M" * n
            elif decimal_bit == 3:
                if 1 <= n < 4:
                    result += 'C' * n
                elif n == 4:
                    result += 'CD'
                elif 9 > n >= 5:
                    result += 'D' + 'C' * (n - 5)
                elif n == 9:
                    result += 'CM'
            elif decimal_bit == 2:
                if 1 <= n < 4:
                    result += 'X' * n
                elif n == 4:
                    result += 'XL'
                elif 9 > n >= 5:
                    result += 'L' + 'X' * (n - 5)
                elif n == 9:
                    result += 'XC'
            elif decimal_bit == 1:
                if 1 <= n < 4:
                    result += 'I' * n
                elif n == 4:
                    result += 'IV'
                elif 9 > n >= 5:
                    result += 'V' + 'I' * (n - 5)
                elif n == 9:
                    result += 'IX'
        return result


print(Solution().intToRoman(58))
