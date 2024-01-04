tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if '<' in tokens[i]:
        print("XML Token")
        count += 1;
    else:
        print("Valid")
    

print(count)