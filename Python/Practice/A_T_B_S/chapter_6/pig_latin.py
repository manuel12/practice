# English to Pig Latin
print('Enter the Englsh message to translate into Pig Latin:')
message = input()

if len(message) == 0:
	message = "My name is AL SWEIGART and I am 4,000 years old." 

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] # A list of words in Pig Latin.
for word in message.split():

	# Separate the non-letters at the start of each word:
	prefix_non_letters = ''
	while len(word) > 0 and not word[0].isalpha():
		prefix_non_letters += word[0]
		word = word[1:]

	if len(word) == 0:
		pig_latin.append(prefix_non_letters)
		continue

	# Separe the non-letters at the end of this word:
	suffix_non_letters = ''
	while not word[-1].isalpha():
		suffix_non_letters += word[-1]
		word = word[:-1]

	# Remember if the word was in uppercase or title case.
	was_upper = word.isupper()
	was_title = word.istitle()

	word = word.lower() # Make the word lowercase for translation.

	# Separate the consonants at the start of the word:
	prefix_consonants = ''
	while len(word) > 0 and not word[0] in VOWELS:
		prefix_consonants += word[0]
		word = word[1:]

	# Add the Pig Latin ending at the end of the word.
	if prefix_consonants != '':
		word += prefix_consonants + 'ay'
	else:
		word += 'yay'

	# Set the word back to uppercase or title case:
	if was_upper:
		word = word.upper()
	if was_title:
		word = word.title()

	# Add the non-letters back to the start or end of the word.
	pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the words back together into a single string:
print(' '.join(pig_latin))