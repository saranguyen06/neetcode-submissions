class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #stack
        closeOpenPairs = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in closeOpenPairs: #c is closing char
                if stack and stack[-1] == closeOpenPairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False