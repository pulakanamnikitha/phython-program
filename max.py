max = int(raw_input())
def largest (arr,n):
  max = arr[0] 
  for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
  return max 
arr = [2,3,1,45,5]
n = len(arr) 
Ans = largest(arr,n) 
print (Ans)
