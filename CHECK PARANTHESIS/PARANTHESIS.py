def checkParanthesis(a):
    res=[]
    for i in range(len(a)):
        if(a[i]=='{' or a[i]=='[' or a[i]=='('):
            res.append(a[i])
        else:
            if(not res):
                return(False)
            else:
                pop=res[-1]
                if(pop=='[' and a[i]==']'):
                    res.pop()
                elif(pop=='{' and a[i]=='}'):
                    res.pop()
                elif(pop=='(' and a[i]==')'):
                    res.pop()
                else:
                    return(False)

    if(res==[]):
        return(True)
    return(False)
n=int(input())
for _ in range(n):
    a=input()
    c=checkParanthesis(a)
    if(c==True):
        print("balanced")
    else:
        print("not balanced")
