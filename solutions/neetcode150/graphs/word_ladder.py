from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # model the problem as a BFS, start from beginWord and stop once we reach endWord
        k = len(beginWord)  # = length of all words in wordList
        q = deque()
        seen = set()
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        CHARS = [chr(char_ord) for char_ord in range(ord('a'), ord('z') + 1)]

        def _get_neighbours(word: str) -> list[str]:
            neighbours = []
            for i in range(k):
                for c in CHARS:
                    nei = word[:i] + c + word[i + 1 :]
                    if nei in word_set:
                        neighbours.append(nei)
            return neighbours

        seen.add(beginWord)
        q.append((beginWord, 1))
        while q:
            word, dist = q.popleft()
            new_dist = dist + 1
            neighbours = _get_neighbours(word)
            for nei in neighbours:
                if nei == endWord:
                    return new_dist
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, new_dist))

        return 0
