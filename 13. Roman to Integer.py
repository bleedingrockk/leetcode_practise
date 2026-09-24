class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        value = 0
        for i, letter in enumerate(s):
            current = roman[letter]

            if i+1 >= len(s):
                value += current

            else:
                print(roman[letter], "and",roman[s[i+1]] )
                if roman[letter] >= roman[s[i+1]]:
                    value += roman[letter]
                else:
                    value -= roman[letter]
        return value



input = "III"
solution = Solution()
print(solution.romanToInt(input))
