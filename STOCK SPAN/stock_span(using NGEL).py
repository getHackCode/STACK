def ngel(arr,n):
    res=[]
    stack=[]
    for i in range(n):
        if(stack==[]):
            stack.append(i)
            res.append(-1)
            continue
        while(stack!=[] and arr[stack[-1]]<=arr[i]):
            stack.pop()
        if(stack==[]):
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(i)
    return(res)
T=int(input())
for _ in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    arr=ngel(l,n)
    result=[]
    for i in range(n):
        result.append(i-arr[i])
    for i in result:
        print(i,end=" ")
    print()
