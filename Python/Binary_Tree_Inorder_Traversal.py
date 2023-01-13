# É um easy, mas nem tão easy. Foi um inferno isso aqui https://leetcode.com/problems/binary-tree-inorder-traversal/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution():
    def inorderTraversal(self, root):
        lista_para_ordernar =[]
        def recursividade(root):
            if not root:
                return [] #retorna uma lista vazia, caso base da recurssão
            else:
                recursividade(root.left) #treenode da esquerda
                lista_para_ordernar.append(root.val)
                recursividade(root.right) #treenode da direita
        recursividade(root)
        return lista_para_ordernar

teste_local = Solution()
print(teste_local.inorderTraversal(TreeNode(2, TreeNode(1), TreeNode(3))))