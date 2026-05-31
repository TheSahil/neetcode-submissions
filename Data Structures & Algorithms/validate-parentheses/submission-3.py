class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        m = {'}':'{', ')':'(', ']':'['}
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0 or stack[-1] != m[s[i]]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0