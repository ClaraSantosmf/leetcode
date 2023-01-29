from Binary_Tree_Inorder_Traversal import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tests_input_simples():
    solution = Solution()
    result = solution.inorderTraversal(TreeNode(2, TreeNode(1), TreeNode(3)))
    assert result == [1, 2, 3]

def tests_input_simples():
    solution = Solution()
    result = solution.inorderTraversal(TreeNode(2, TreeNode(1, TreeNode(3)), TreeNode(3)))
    assert result == [3, 1, 2, 3]
