class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
            else:
                start, nex = stack.pop(), stack.pop()
                op = tokens[i]
                if op == "+":
                    stack.append(start + nex)
                elif op == "-":
                    stack.append(nex - start)
                elif op == "*":
                    stack.append(start * nex)
                elif op == "/":
                    stack.append(int(nex / start))
        
        return stack[-1]