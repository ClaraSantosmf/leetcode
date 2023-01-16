#Esse problema é um MEDIUM https://leetcode.com/problems/reverse-integer/description/
# Esse algoritmo é de trocar final e começo corresponde ao que a biblioteca revert do python faz. Esse é um algoritmo relacionado ao array ou arranjo. 

class Solution:
    def reverse(self, x: int) -> int:
        negativo = False
        if (x>-9) and (x<9):
            return x
        if x < 0:
            negativo = True
            x=x*(-1)
        x = str(x)
        x = list(x)
        inicio = 0
        final = len(x) - 1
        while inicio < final:
            x[inicio], x[final] = x[final], x[inicio]
            inicio += 1
            final -= 1
        x = ''.join(x)
        if negativo:
            x = int(x) * (-1)
        else:
            x = int(x)
        if (x>-2**31) and x < (2**31)-1:
            return x
        else:
            return 0

testando_localmente = Solution()
print(f'Espera que o resultado seja 321: {testando_localmente.reverse(123)}')
print(f'Espera que o resultado seja 0: {testando_localmente.reverse(1534236469)}')
print(f'Espera que o resultado seja 0: {testando_localmente.reverse(0)}')
print(f'Espera que o resultado seja 0: {testando_localmente.reverse(-8)}')
