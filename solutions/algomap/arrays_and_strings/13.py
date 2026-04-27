class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numeral_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        compound_roman_numerals = ('IV', 'IX', 'XL', 'XC', 'CD', 'CM')

        value = 0

        i = 0
        while i < len(s):
            if s[i : i + 2] in compound_roman_numerals:
                value += roman_numeral_values[s[i + 1]] - roman_numeral_values[s[i]]
                i += 2
            else:
                value += roman_numeral_values[s[i]]
                i += 1

        return value
