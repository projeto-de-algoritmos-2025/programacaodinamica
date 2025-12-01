# transformar o array inicial no array que será dado usando o menor número possível de operações.                  class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
    
        min_total_operations = 0
        prev_height = 0 
    
        for current_height in target:
            if current_height > prev_height:
                new_increments_needed = current_height - prev_height
                min_total_operations += new_increments_needed
        
            prev_height = current_height
        
        return min_total_operations