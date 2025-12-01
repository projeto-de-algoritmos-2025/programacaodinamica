import math

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        max_bits = n.bit_length()

        # dp[k] = Mín. operações para transformar 2^k em 0. (2^(k+1) - 1)
        dp = [0] * (max_bits + 1)
        dp[0] = 1 
    
        for k in range(1, max_bits):
            dp[k] = 2 * dp[k-1] + 1
    
        return solve(n)