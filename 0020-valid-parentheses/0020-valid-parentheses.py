class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == '(' or s[i] == '{' or s[i] == '[':
        #         stack.append(s[i])
        #     else:
        #         if len(stack) ==0:
        #             return False
        #         top = stack.pop()
        #         if top == '(' and s[i] != ')':
        #             return False
        #         if top == '[' and s[i] != ']':
        #             return False
        #         if top == '{' and s[i] != '}':
        #             return False
        #         if top == None:
        #             return False
        # if len(stack)>0:
        #     return False
        # return True
        stack= []
        dic = {"}":"{", "]":"[",")":"("}
        for i in s:
            if i in dic:
                if stack and stack[-1]== dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
