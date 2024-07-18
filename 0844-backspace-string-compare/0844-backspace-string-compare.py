class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1 = []
        stk2 = []
        
        for char in s:
            if char == '#':
                if len(stk1) != 0:
                    stk1.pop()
                else:
                    continue
            else:
                stk1.append(char)
        
        for char in t:
            if char == '#':
                if len(stk2) != 0:
                    stk2.pop()
                else:
                    continue
            else:
                stk2.append(char)
        
        return stk1 == stk2