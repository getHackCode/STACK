class Solution:
    def celebrity(self, M, n):
        if(n<2):
            return(-1)
        
        def knows(M,a,b):
            return(M[a][b])
        a=[0]*n
        b=-1
        c=0
        for i in range(n):
            if(M[i]==a):
                b=i
        if(b==-1):
            return(-1)
        
        
        for i in range(n):
            if(i==b):
                continue
            else:
                if(knows(M,i,b)==1):
                    c=c+1
    
        if(c==n-1):
            return(b)
        else:
            return(-1)
