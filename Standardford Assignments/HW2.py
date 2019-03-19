
import statistics
import math 
def Calculate_ConfidenceInternal(L):
	mn = statistics.mean(L)

	print("mean=", mn)
	std =0 
	sum =0
	for i in range(len(L)):
		sum = sum + math.pow(L[i]-mn,2)
	
	std =math.sqrt((sum /(len(L)-1)))
	print ("Standard DEviation =", std)
	print ("Confirm STDEV by inbuilt function= ", statistics.stdev(L))	

	CI = 1.645 * (std /math.sqrt((len(L))))

	print("We are 95% Confident that true mean for highht will be between ",  mn-CI, mn+CI,)


L =[150,160,155, 161, 153]	
Calculate_ConfidenceInternal (L)




