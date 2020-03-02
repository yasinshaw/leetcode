import math


class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        res = 0
        num_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        max = int(math.pow(2, 31)) - 1
        length = len(str)

        while i < length and str[i] == ' ':
            i += 1

        if i < length:
            if str[i] == '-':
                sign = -1
                i += 1
            elif str[i] == '+':
                sign = 1
                i += 1
            elif str[i] not in num_map:
                return 0

        while i < length:
            if str[i] not in num_map:
                break
            res = res * 10 + num_map[str[i]]
            i += 1
        if res > max:
            if sign == 1:
                res = max
            if sign == -1:
                res = max + 1
        return res * sign
