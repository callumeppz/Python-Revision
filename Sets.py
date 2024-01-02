countries = ['Angola', 'Maldives', 'India']
country_set = set(countries)
print('India' in countries) #true
country_set.add('Italy') #adds italy to the set
newCountrySet = country_set.pop() # removes one value and sets to another varaible
print (newCountrySet)
print (country_set)