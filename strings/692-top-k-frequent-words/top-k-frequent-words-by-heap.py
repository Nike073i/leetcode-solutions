# memory: O(n + k), где n - кол-во уникальных слов, k - элементов
# time: O(n log k)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        heap = []
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
