from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
 
    if not root:
        return []
    
    output = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if node:
            output.append(node.val)
            # Adiciona os filhos para manter a estrutura correta.
            queue.append(node.left)
            queue.append(node.right)
        else:
            output.append(None)

    # Remove os 'None's finais
    while output and output[-1] is None:
        output.pop()
        
    return output

# Caso 2: Árvore de 3 nós (Completa - Esquerda)
#      0
#     / \
#    0   0
# Estrutura: [0, 0, 0]
root2 = TreeNode(0, TreeNode(0), TreeNode(0))
list2 = tree_to_list(root2)
print(f"Árvore 3 Nós FBT: {list2}")
# Esperado: [0, 0, 0]