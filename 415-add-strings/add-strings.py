class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #It lets you work with much bigger numbers written as strings.
        sys.set_int_max_str_digits(10000)
        return str(int(num1) + int(num2))
        