# PROBLEMA EASYYY
# https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums):
        tamanho_da_lista = len(nums)//2
        dicionario = {i:0 for i in nums}
        for i in nums:
            if dicionario[i]+1>tamanho_da_lista:
                return i
            else:
                dicionario[i] += 1