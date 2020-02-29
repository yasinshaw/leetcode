class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n = len(a)
        m = len(b)
        i, j = n - 1, m - 1
        res = []
        while i >= 0 or j >= 0:
            char_a = int(a[i]) if i >= 0 else 0
            char_b = int(b[j]) if j >= 0 else 0
            temp = char_a + char_b + carry
            carry = 1 if temp > 1 else 0
            res.insert(0, temp % 2)
            i -= 1
            j -= 1
        if carry == 1:
            res.insert(0, 1)
        return ''.join(list(map(str, res)))
