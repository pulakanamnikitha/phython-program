n=list(raw_input())
for i in range(0,len(n)-1,2):
    n[i],n[i+1]=n[i+1],n[i]
print("".join(str(x) for x in n))
