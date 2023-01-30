from majori import Solution

def test_input_simples():
    solution = Solution()
    nums = [3,2,3]
    result = solution.majorityElement(nums)
    assert result == 3


def test_input_mais_complexo():
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    result = solution.majorityElement(nums)
    assert result == 2
