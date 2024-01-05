# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for i in range(1, number+1): # factorial using for loop, needs to start from 1
    product*=i
    
# print the factorial of number
print(product)