countries = ['Angola', 'Maldives', 'India']
country_set = set(countries)
print('India' in countries) #true
country_set.add('Italy') #adds italy to the set
newCountrySet = country_set.pop() # removes one value and sets to another varaible
print (newCountrySet)
print (country_set)


a = [1, 2, 2, 6, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
print(b)

# maybe 5