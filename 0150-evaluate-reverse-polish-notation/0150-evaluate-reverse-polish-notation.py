from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()
        cur_ans = None
        for token in tokens:
            if token.lstrip('-').isdigit():
                s.append(int(token))
            else:
                operand2 = s.pop()
                operand1 = s.pop()
                if token == '+':
                    s.append(operand1 + operand2)
                elif token == '-':
                    s.append(operand1 - operand2)
                elif token == '*':
                    s.append(operand1 * operand2)
                else:
                    s.append(int(operand1 / operand2))
        return s.pop()

