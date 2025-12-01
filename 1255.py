from collections import Counter

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
                
        initial_counts = Counter(letters)
        
        char_scores = {chr(ord('a') + i): score[i] for i in range(26)}
        
        word_data = []
        for word in words:
            word_count = Counter(word)
            word_score = sum(char_scores.get(char, 0) * count for char, count in word_count.items())
            word_data.append({'score': word_score, 'counts': word_count})

        memo = {}
                
        def dp(index: int, counts_tuple: tuple) -> int:
            
            current_counts = Counter({chr(ord('a') + i): count 
                                      for i, count in enumerate(counts_tuple) if count > 0})
            
            state = (index, counts_tuple)
            if state in memo:
                return memo[state]
            
            if index == len(words):
                return 0
            
            
            score_if_skip = dp(index + 1, counts_tuple)
            
            
            
            current_word_info = word_data[index]
            score_if_take = 0
            can_take = True
            
            new_counts = current_counts.copy()
            for char, required in current_word_info['counts'].items():
                if required > current_counts[char]:
                    can_take = False
                    break
                new_counts[char] -= required
            
            if can_take:
                new_counts_tuple = [new_counts.get(chr(ord('a')), 0) for i in range(26)]
                new_counts_tuple = tuple(new_counts_tuple)
                
                score_if_take = current_word_info['score'] + dp(index + 1, new_counts_tuple)
            
            
            result = max(score_if_skip, score_if_take)
            
            memo[state] = result
            return result

        
        initial_counts_tuple = tuple(initial_counts.get(chr(ord('a')), 0) for i in range(26))
        
        return dp(0, initial_counts_tuple)