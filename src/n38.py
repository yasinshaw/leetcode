class Solution:
    def countAndSay(self, n: int) -> str:
        res = [1]
        for i in range(1, n):
            temp = []
            str_len = len(res)
            j = 0
            while j < str_len:
                k = j + 1
                while k < str_len and res[k] == res[k - 1]:
                    k += 1
                temp.append(k - j)
                temp.append(res[j])
                j += k - j
            res = temp
        return ''.join(list(map(str, res)))
