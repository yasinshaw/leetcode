class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        # 贪心算法，由大到小，这里key需要有序。
        for key in hash_map:
            if num // key != 0:
                count = num // key
                res += hash_map[key] * count
                num %= key
        return res
