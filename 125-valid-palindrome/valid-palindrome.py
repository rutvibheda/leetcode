class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for letter in s:
            if letter.isalnum():
                result.append(letter.lower())
        result = ''.join(result)
        return result == result[::-1]
                   