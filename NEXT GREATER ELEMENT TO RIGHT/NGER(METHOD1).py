def nger(A,N):
    stack=[]
    res={}
    for i in A:
        if(stack==[]):
            stack.append(i)
            continue
        while(stack!=[] and stack[-1]<i):
            res[stack[-1]]=i
            stack.pop()
        stack.append(i)
    for i in A:
        if(i not in res):
            print(-1,end=" ")
        else:
            print(res[i],end=" ")
            
    print()
    return(res)
t=int(input())
for _ in range(t):
    N=int(input())
    A=list(map(int,input().split()))
    nger(A,N)
    
