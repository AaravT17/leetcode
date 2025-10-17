class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Approach 1
        # result = ''

        # for i in range(min(len(word1), len(word2))):
        #     result += word1[i] + word2[i]

        # if(len(word1) > len(word2)):
        #     result += word1[len(word2):]
        # elif(len(word2) > len(word1)):
        #     result += word2[len(word1):]

        # return result
        # The issue with this approach is that, in Python, strings are immutable,
        # so each time we append a character, a new string must be created so the
        # whole string gets copied over, which is O(n) time, making this an
        # inefficient approach

        # Approach 2
        result = []
        # Appending to a list is O(1) time on average
        shorter_word_length = min(len(word1), len(word2))

        for i in range(shorter_word_length):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > len(word2):
            for i in range(shorter_word_length, len(word1)):
                result.append(word1[i])
        elif len(word2) > len(word1):
            for i in range(shorter_word_length, len(word2)):
                result.append(word2[i])

        return ''.join(result)
