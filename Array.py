names = ["Callum", "Apps"]
print (names[1])

names[1] = "changed"
print (names)
print (len(names)) # returns length of array

numbers = [1,3,5,2,7,8]
numbersSorted = sorted(numbers) # sort an array
print (numbersSorted)

print (min(numbersSorted)) # min and max of array
print (max(numbersSorted))

name = "-".join(["Callum", "Apps"]) # Join function adds "-"
print(name)

letters = ['a', 'b', 'c', 'd'] # using append to add to the list
letters.append('z')
print(letters)