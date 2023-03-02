class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return next(zip(*Counter(sorted(words)).most_common(k)))
