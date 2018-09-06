a=int(raw_input())
j=0
for i in range(2,a//2+1):
    if(a%i==0):
        j=j+1
if(j<=0):
    print("yes")
else:
    print("no")
