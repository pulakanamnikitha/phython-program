n=int(raw_input())
pro=1
while n>0:
    dig=n%10
    pro=pro*dig
    n=n/10
print pro
