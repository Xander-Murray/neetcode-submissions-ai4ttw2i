class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for thing in tokens: 
            if thing == '+':
                stack.append(stack.pop() + stack.pop())
            elif thing == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif thing == '*':
                stack.append(stack.pop() * stack.pop())
            elif thing == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(thing))
        return stack[0]



        