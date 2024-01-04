points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 51:
    prize = 'Wooden Rabbit'
elif points <= 1810:
    prize = "Wafer-thin mint"
else:
    prize = "Penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = ("Congratulations! You won a {}!".format(prize))
else:
    result = ("Oh dear, no prize this time.")


print(result)