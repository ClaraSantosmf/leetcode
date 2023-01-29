from Decode_Ways import Solution

def test_input_simples():
    solution = Solution()
    numeroDeCombinacoesPossiveis = solution.numDecodings("1111")
    assert numeroDeCombinacoesPossiveis == 5

def test_input_esquisito():
    solution = Solution()
    numeroDeCombinacoesPossiveis = solution.numDecodings("2101")
    assert numeroDeCombinacoesPossiveis == 1

    ## verificar esse teste aqui em. 

def test_input_arromba_memoria():
    solution = Solution()
    numeroDeCombinacoesPossiveis = solution.numDecodings("11111111111111111111111111111111111111111")
    assert numeroDeCombinacoesPossiveis == 267914296

