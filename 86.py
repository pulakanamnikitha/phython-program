q=raw_input()
c=len(q)
fct=0
for i in range(0,c):
    j=i+1
    while j<c:
        if ord(q[i])==ord(q[j]):
            fct=1
        j=j+1
if fct!=1:
    print "Yes"
else:
    print "No"
