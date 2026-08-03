class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=['+', '-', '*', "/"]
        ans=0
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token in ops:
                num2=int(stack.pop())
                num1=int(stack.pop())
                if token == "+":
                    ans=num1+num2
                if token == "-":
                    ans=num1-num2
                if token == "*":
                    ans=num1*num2
                if token == "/":
                    ans=num1/num2
                    
                stack.append(ans)
            else:
                stack.append(token) 
        return int(ans)
        