##############
# Q1
###############
a = 5
b = 7
c = a + b
print(c)

##############
# Q2
###############
answer = 0
for i in range(1,101):
    answer = answer + i
print(answer)

##############
# Q3
###############
def number_sum (final_number):
    if final_number >=1:
        # Check to see that the input is correct
        answer = 0
        for i in range(1,final_number+1): #note in python the final number is not included so if you type range(1,100) it will go from 1 to 99.
            answer = answer +i

    else:
        print("Input must be a positive number >1")
        answer = None
    return answer

number_sum(100)

##############
# Q4
###############
def number_sum_formula (final_number):
    if final_number >=1:
        # Check to see that the input is correct
        answer = final_number * (final_number+1)/2
    else:
        print("Input must be a positive number >1")
        answer = None
    return answer

number_sum_formula (100)
