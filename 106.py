def findK(n,s): 
    half=int((n+1)/2) 
    if s>n: 
        return(2*(s-half)) 
    else: 
        return(2*s - 1) 
n=5
s=3
print(findK(n,s)) 
