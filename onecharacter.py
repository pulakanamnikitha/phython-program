s,n=map(str,raw_input().split())
c=0
for i in range(len(s)):
    if s[i]!=n[i]:
        c=c+1
if(c==1):
    print('yes')
else:
    print('no')
