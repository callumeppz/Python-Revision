book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {} # initialising empty dictionary
word_counter2 = {} # initialising empty dictionary

for word in book_title:
    if word not in word_counter:
            word_counter[word] = 1 # initilalising the word with 1 if not in dictionary
    else:
            word_counter[word] += 1 # adding an extra 1 to word counter if word already appears in dictionary

print(word_counter) # printing word_counter dictionary

for word in book_title:
    word_counter2[word] = word_counter.get(word, 0) + 1 # another way of completing word count, using get method


print(word_counter2) # printing word_counter dictionary