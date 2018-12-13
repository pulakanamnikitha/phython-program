x,y=map(int,raw_input().split())
if x > y:  
   greater = x  
else:  
   greater = y  
while(True):  
   if((greater % x == 0) and (greater % y == 0)):  
        lcm = greater  
        break  
   greater =  greater + 1
print ( lcm)
