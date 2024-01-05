x = input("Enter Age") # user input
x = int(x) # required to change input from str to int

ChildTicket = 2
AdolecentTicket = 4
AdultTicket = 6

if x < 0: # checks for valid input 
    x = "Enter a Valid Age"
elif x <= 8: # various conditional statements to check input compared to condition
    x = "Ticket price is ${} because they are {} years old".format(ChildTicket, x) # format used as efficient means to use x and ticket prices delcared previously
elif x <= 18:
    x = "Ticket price is ${} because they are {} years old".format(AdolecentTicket, x)
elif x <= 50:
    x = "Ticket price is ${} because they are {} years old".format(AdultTicket, x)
else:
    x = "Ticket Price is free due to age being more than 50, {}".format(x)

print(x) # print at the end43