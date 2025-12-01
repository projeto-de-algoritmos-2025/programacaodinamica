# formar um conjunto válido de palavras a partir da lista
#de palavras fornecida, que maximize a pontuação total

from collections import Counter

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
                
        initial_counts = Counter(letters)
        
        initial_counts_tuple = tuple(initial_counts.get(chr(ord('a') + i), 0) for i in range(26))
        
        
        char_scores = {chr(ord('a') + i): score[i] for i in range(26)}
        
        word_data = []
        for word in words:
            word_count = Counter(word)
            
            word_score = sum(char_scores.get(char, 0) * count for char, count in word_count.items())
            
            word_data.append({'score': word_score, 'counts': word_count})
        
        # (index, counts_tuple) -> max_score
        memo = {}