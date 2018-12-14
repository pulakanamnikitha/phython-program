def sort(values):
	for  i in range(len(values)):		
		for r in range(i, len(values)):			
			if (values[i] > values[r]):
				temp = values[i]
				values[i] = values[r]
				values[r] = temp
x = raw_input().rstrip()
xList = list(x)
sort(xList)
print("".join(xList))
