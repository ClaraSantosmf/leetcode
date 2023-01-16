class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        inicio = 0
        fim = len(s) -1
        while inicio < fim:
            s[inicio], s[fim] = s[fim], s[inicio]
            inicio += 1
            fim -=1
        return s

a = Solution()
s = ["h","e","l","l","o"]
print(f"O resultado disso deveria ser ['o', 'l', 'l', 'e', 'h']: {a.reverseString(s)}")