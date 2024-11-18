class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack =[]
        # for i in tokens:
        #     if i == "+" or i =="*" or i == "-" or i == "/":
        #         if i =="/":
        #             i= "//"
        #         x = stack.pop()
        #         y = stack.pop()
        #         z = eval(y + i + x)
        #         stack.append(int(z))
        #     else:
        #         stack.append(i)
        # return stack[-1]


        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]



         