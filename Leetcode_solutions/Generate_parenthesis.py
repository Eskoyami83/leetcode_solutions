def generateParenthesis(self, n):
        stack=[]
        res=[]
        
        def bactrack(opend,closed):
            if opend==closed==n:
                res.append("".join(stack))
            if opend<n:
                stack.append("(")
                bactrack(opend+1,closed)
                stack.pop()
            if closed<opend:
                stack.append(")")
                bactrack(opend,closed+1)
                stack.pop()
        
        bactrack(0,0)
        return res