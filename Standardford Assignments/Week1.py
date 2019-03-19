def countnumbers(n):
	
	""" sum of the numbers upto the give number n"""
	total =0
	for i in range(n+1):
		total=total+i
	return total

def findmedian(n):
	return (n*(n+1))/2

print(countnumbers(50))
print(findmedian(50))		