class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = { ')' : '(', '}' : '{' , ']' : '['}    
        stack = []
        for bracket in s:
            if bracket in brackets_dict:
                if stack and stack[-1] == brackets_dict[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True