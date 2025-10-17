class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = {}
        for char in magazine:
            if char in magazine_chars:
                magazine_chars[char] += 1
            else:
                magazine_chars[char] = 1

        for char in ransomNote:
            if char not in magazine_chars or magazine_chars[char] == 0:
                return False
            magazine_chars[char] -= 1

        return True
