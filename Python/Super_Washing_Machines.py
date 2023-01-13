## HARD Super Washing Machines https://leetcode.com/problems/super-washing-machines/description/
## Esse BO é que nem a torre de hanoi, pq mexe com movimentos e regras. Dava para fazer com recursão. Mas o leetcode tem mania de colocar uns inputs nojentos que estouram a memoria. Então vamos com base na função max.
## Função max pode receber key. Essa é responsável por ser uma chave de comparação final. Então ultima linha do for é comparado se o maior numero de movimentos é maior ou menor ao numero de movimento mais alto encontrado na ultima iteração por meio do método abs. 

class Solution:
    def findMinMoves(self, machines):
        qtd_de_maquina = len(machines)
        qtd_de_roupa = sum(machines)
        if qtd_de_roupa % qtd_de_maquina == 0:
            qtd_de_roupas_em_maquinas = qtd_de_roupa/qtd_de_maquina
            movimento_total = 0
            movimento = 0
            for i in range(qtd_de_maquina):
                roupas_que_faltam = machines[i] - qtd_de_roupas_em_maquinas
                movimento = movimento+ roupas_que_faltam
                movimento_total = max(movimento_total, roupas_que_faltam, abs(movimento))
            return int(movimento_total)
        else:
            return -1

testando_localmente = Solution()
maquinas = [1,0,5]
testando_localmente.findMinMoves(maquinas)