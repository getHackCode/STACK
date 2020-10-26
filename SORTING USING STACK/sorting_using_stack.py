#####MY SOLUTION GIVES THE ARRAY IN DESCENDING ORDER OF SORTING
def sorted(s):
    a=[]
    while(s!=[]):
        b=s.pop()
        if(a==[]):
            a.append(b)
            continue
        else:
            while(a!=[] and a[-1]<b):
                s.append(a.pop())
            a.append(b)
    for i in a:
        print(i,end=" ")
n=list(map(int,input().split()))
sorted(n)
