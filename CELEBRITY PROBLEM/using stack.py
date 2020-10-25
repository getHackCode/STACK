class Solution:
    def celebrity(self, M, n):
        def knows(M,a,b):
            if(M[a][b]==1):
                return(True)
            return(False)
        stack=[i for i in range(n)]
        while(len(stack)>1):
            a=stack.pop()
            b=stack.pop()
            if(M[a][b]==1):
                stack.append(b)
            else:
                stack.append(a)
        if(stack==[]):
            return(-1)
        a=stack.pop()
        for i in range(n):
            if(i==a):
                continue
            if(knows(M,a,i) or not knows(M,i,a)):
                return(-1)
        return(a)
        
