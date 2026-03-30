class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMapClosedToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in hashMapClosedToOpen:
                if stack and stack[-1] == hashMapClosedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
        
