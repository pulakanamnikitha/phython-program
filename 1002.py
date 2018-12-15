r=int(raw_input())
pro=1
while r>0:
    dig=r%10
    pro=pro*dig
    r=r/10
print pro
