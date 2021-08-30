# https://leetcode.com/problems/valid-parentheses/solution/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                d = stack.pop()
                if (d == '(' and not c ==')') or (d == '[' and not c ==']') or (d == '{' and not c =='}'):
                    return False
        if len(stack) > 0:
            return False
        return True