class Solution : 
    def pair(self,open, close):
        if open =='(' and close==')':
            return True
        if open =='[' and close==']':
            return True
        if open =='{' and close=='}':
            return True
        

    def valid_pranthesis(self, expression):
        stack = []

        for exp in expression: 
            if exp == '(' or exp == '{' or exp == '[':
                stack.append(exp)

            elif exp == ')' or exp == '}' or exp == ']':
                if len(stack) == 0 or not self.pair(stack[-1], exp):
                    return False
                else : 
                    stack.pop()


        return len(stack) == 0
    

s = Solution()
expression = input('Enter the expression')
print(s.valid_pranthesis(expression))