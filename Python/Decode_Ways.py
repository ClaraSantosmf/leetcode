## Esse é um MEDIUM que envolve a busca por profundidade. Mais informações existem nesse incrível link do Instituto de matemática e estatistica da USP  https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/dfs.html#:~:text=Um%20algoritmo%20de%20busca%20(ou,em%20que%20visita%20os%20v%C3%A9rtices.
# Para busca por profundidade, o caso usa recursão. E como todo caso de uso de recursão, o problema reside em ESTOURAR LOUCAMENTE A MEMORIA. 
# Para não estourar a memoria, usamos a biblioteca lru_cache.

from functools import lru_cache

class Solution:
    @lru_cache(maxsize = None)
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": 
            return 0 #Caso base da recursão. Caso comece com 0, esse número não poderá ser combinado
        if len(s) == 1:
            return 1 #Se só vier um elemento, só existe uma possibilidade de combinação 
        if int(s) in range(1, 27):
            combinacoes = 1
        else:
            combinacoes = 0
        i = 1
        while int(s[:i]) in range(1, 27) and i < len(s):
            combinacoes += self.numDecodings(s[i:]) #Chamando na recursão
            i += 1
        return combinacoes

##Teste local

a = Solution()
print(a.numDecodings("1111"))
print(a.numDecodings("2101"))
print(a.numDecodings("11111111111111111111111111111111111111111"))
