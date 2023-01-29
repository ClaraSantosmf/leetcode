# É um easy, mas nem tão easy. Foi um inferno isso aqui https://leetcode.com/problems/binary-tree-inorder-traversal/

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
        