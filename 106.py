def findK(n,s): 
    half=int((n+1)/2) 
    if s>n: 
        return(2*(s-half)) 
    else: 
        return(2*s - 1) 
n=4
s=2
print(findK(n,s)) 
