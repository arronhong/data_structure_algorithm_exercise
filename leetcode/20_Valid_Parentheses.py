class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_by_right = {'}': '{',
                         ']': '[',
                         ')': '('}
        for c in s:
            if c in ['{', '[', '(']:
                stack.append(c)
                continue

            try:
                if stack.pop() != left_by_right[c]:
                    return False
            except IndexError:
                return False

        if stack:
            return False
        return True