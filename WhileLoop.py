# number to find the factorial of
number = int(input("enter num"))

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number: # find factorial, whilst current is smaller than the number given
    product *= current # multiply current with product
    current += 1 # add to current
    
# print the factorial of number
print(product)