names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in names:
    i = i.replace(' ','_')
    usernames.append(i.lower())

print(usernames)