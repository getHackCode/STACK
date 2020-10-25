def Push(x,stack1,stack2):
    while(stack1):
        stack2.append(stack1.pop())
    stack1.append(x)
    while(stack2):
        stack1.append(stack2.pop())
    
def Pop(stack1,stack2):
    if(not stack1):
        return(-1)
    return(stack1.pop())
