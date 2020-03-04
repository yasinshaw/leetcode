class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n = len(a)
        m = len(b)
        i, j = n - 1, m - 1
        res = []
        while i >= 0 or j >= 0:
            if i >= 0 and a[i] == '1':
                carry += 1
            if j >= 0 and b[j] == '1':
                carry += 1
            res.append(carry % 2)
            i -= 1
            j -= 1
            carry //= 2
        if carry == 1:
            res.append(1)
        res.reverse()
        return ''.join(list(map(str, res)))
