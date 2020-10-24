def nger(A,N):
    stack=[]
    res=[]
    for i in A[::-1]:
        if(stack==[]):
            stack.append(i)
            res.append(-1)
            continue
        while(stack!=[] and stack[-1]<i):
            stack.pop()
        if(stack==[]):
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(i)
    for i in res[::-1]:
        print(i,end=" ")
    print()
t=int(input())
for _ in range(t):
    N=int(input())
    A=list(map(int,input().split()))
    nger(A,N)
