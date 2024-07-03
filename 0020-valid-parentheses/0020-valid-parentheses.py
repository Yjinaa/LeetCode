from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        s = list(s)
        chk = 0
        for elem in s:
            if elem == '(' or elem == '[' or elem == '{':
                stack.append(elem)
                chk += 1
            else:
                if len(stack) != 0:
                    if elem == ')':
                        if stack.pop() != '(':
                            return False
                        else:
                            chk -= 1
                    elif elem == ']':
                        if stack.pop() != '[':
                            return False
                        else:
                            chk -= 1
                    elif elem == '}':
                        if stack.pop() != '{':
                            return False
                        else:
                            chk -= 1
                else:
                    return False
        if chk != 0:
            return False
        else:
            return True


