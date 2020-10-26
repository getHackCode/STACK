def calculateSpan(A,n):
    ans =[0]*n
    ans[0] = 1
    for i in range(1, n): 
        counter = 1
        while ((i - counter) >= 0 and A[i] >= A[i - counter]): 
            counter += ans[i - counter] 
        ans[i] = counter 
    return(ans)
calculatespan([1,3,5,3,6,34,6,4,6,4,5,6,3],13)
