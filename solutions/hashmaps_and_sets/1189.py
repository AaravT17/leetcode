from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Approach 1
        # s = 'balloon'
        # count = 0
        # text_chars = {}
        # for char in text:
        #     if char in text_chars:
        #         text_chars[char] += 1
        #     else:
        #         text_chars[char] = 1

        # curr_index = 0
        # while s[curr_index] in text_chars:
        #     if text_chars[s[curr_index]] == 1:
        #         del text_chars[s[curr_index]]
        #     else:
        #         text_chars[s[curr_index]] -= 1
        #     if curr_index == len(s) - 1:
        #         count += 1
        #         curr_index = 0
        #     else:
        #         curr_index += 1

        # return count

        # Approach 2
        s_chars = Counter('balloon')

        relevant_text_chars = {}
        for char in text:
            if char in s_chars:
                if char in relevant_text_chars:
                    relevant_text_chars[char] += 1
                else:
                    relevant_text_chars[char] = 1

        possible_words = float('inf')
        for char in s_chars:
            if char not in relevant_text_chars:
                return 0
            possible_words = min(
                possible_words, relevant_text_chars[char] // s_chars[char]
            )

        return possible_words
