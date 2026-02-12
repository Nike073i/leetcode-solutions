# memory: O(m), где m - кол-во уникальных слов
# time: O(n + m log m), где n - кол-во всех слов, m - кол-во уникальных
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        sorted_words = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        return sorted_words[:k]
