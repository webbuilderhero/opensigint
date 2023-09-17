# TODO: test, optimize

# Decoder for RFSM FLARQ

import csv

# define lists to store data
codewords = []
words = []

# read in codewords and translate words
with open('codeword_dictionary.csv', encoding='utf-8-sig') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		codewords.append(row[0])
		words.append(row[1])

# define function to decode
def decode_rfsm_flarq(codeword):
	''' Decodes the given codeword using the RFSM FLARQ protocol.
		
		Args:
			codeword(str): Codeword as a string
		
		Returns:
			translated_word(str): The translated word or empty string if not found
	'''
	translated_word = ""
	# loop through codewords
	for i in range(len(codewords)):
		# check if codeword is present
		if codeword == codewords[i]:
			# store corresponding translated word
			translated_word = words[i]
			# stop looping
			break
	return translated_word

# test code
word = "9919"
decoded = decode_rfsm_flarq(word)

if(decoded == "location"):
	print("Test passed. Word {} decoded to {}".format(word, decoded))
else:
	print("Test failed. Word {} decoded to {}, expected 'location'".format(word, decoded))