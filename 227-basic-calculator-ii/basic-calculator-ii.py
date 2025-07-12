class Solution:
    def calculate(self, s: str) -> int:

        num = 0
        s = s + '+'
        previous_sign = '+'
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-*/':
                if previous_sign == '+':
                    stack.append(num)
                elif previous_sign == '-':
                    stack.append(-num)
                elif previous_sign == '*':
                    stack.append(stack.pop() * num)
                elif previous_sign == '/':
                    stack.append(math.trunc(stack.pop() / num))
                
                previous_sign = c
                num = 0
     
        return sum(stack)

                
