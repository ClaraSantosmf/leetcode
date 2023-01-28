#Esse problema é um MEDIUM https://leetcode.com/problems/group-anagrams/
# resolução sem recursividade com dicionário. Um péssimo desempenho. 

class Solution:
    def groupAnagrams(self, strs):
        dicts_de_palavras = {}
        anagramas =[]
        for palavra in strs:
            dicts_de_palavras[palavra]={letra:0 for letra in palavra}
            for letras in palavra:
                if letras in dicts_de_palavras[palavra]:
                    dicts_de_palavras[palavra][letras] += 1 
        cache = []
        nova_lista =[]
        for parametro in dicts_de_palavras:
            if parametro not in cache:
                for j in range(len(strs)):
                    if dicts_de_palavras[parametro] == dicts_de_palavras[strs[j]]:
                        nova_lista.append(strs[j])
                        cache.append(strs[j])

            if nova_lista:
                anagramas.append(nova_lista)
                nova_lista =[]
        return anagramas

