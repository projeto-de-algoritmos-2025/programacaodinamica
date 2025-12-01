import math

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        max_bits = n.bit_length()

        dp = [0] * (max_bits + 1)
        dp[0] = 1 
    
        for k in range(1, max_bits):
            dp[k] = 2 * dp[k-1] + 1

        def solve(current_n):
            if current_n == 0:
                return 0
        
            k = current_n.bit_length() - 1
            power_of_2 = 1 << k
        
            remainder = current_n ^ power_of_2 
        
            return dp[k] - solve(remainder)
    
        return solve(n)