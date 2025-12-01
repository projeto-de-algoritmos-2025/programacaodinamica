from typing import List, Optional, Dict

class Solution:
    def __init__(self):

        self.memo: Dict[int, List[Optional[TreeNode]]] = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[Optional[TreeNode]]:
        
        if N % 2 == 0:
            return []
        
        if N in self.memo:
            return self.memo[N]
        
        result = []
        
        for L in range(1, N, 2):
            R = N - 1 - L  

            left_trees = self.allPossibleFBT(L)
            right_trees = self.allPossibleFBT(R)
            
            for left_root in left_trees:
                for right_root in right_trees:
                    root = TreeNode(0) 
                    root.left = left_root
                    root.right = right_root
                    result.append(root)
        
        self.memo[N] = result
        return result

solution = Solution()
fbt_list = solution.allPossibleFBT(7)
print(f"Número de FBTs possíveis para N=7: {len(fbt_list)}")
