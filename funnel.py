def read_file():
	""" This function reads the file enable1.txt that contains a list of English words, and returns a python list of those words """
	file = open("enable1.txt", "r") 
	words = []
	
	for line in file:
		line = line.strip()
		words.append(line)

	return words

def char_to_index(char):
	""" Returns the index of a character in the alpbabet, eg. 'a' would be 0, 'z' would be 25. """
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for c in range(len(alphabet)):
		if (alphabet[c] == char):
			return c
			
	return False # char was not in the alphabet

def word_exists(word):
	""" Uses a binary search to check if 'word' is present in the enable1.txt list """
	words = read_file()
	low = 0 # the initial lower bound of the binary search
	high = len( words ) - 1 # the initial higher bound of the binary search is the length of the list of words
	index = binary_search(word, words, high, low) # call 'binary_search' find the index of that word in the list
	return index # will be false if the word wasn't found
		  	  
def binary_search(word, words, high, low):
	""" A binary search to check if word is in words and at what index.
	word - the word being searched
	words - the list of words 
	high - the higher bound of the binary search
	low - the lower bound of the binary search"""
	if (high < low):
		return False # if the higher bound becomes less than the lower then the word was not found in words
		
	mid = round( (low + high) / 2 ) # take the middle word in the list
	
	if ( precedes ( word, words[mid] ) ): # if the search word precedes the current word alphabetically
		return binary_search(word, words, mid-1, low) # search in the 1st half of the list by making the current midpoint the new higher bound
	elif ( precedes ( words[mid] , word ) ): # if the current word precedes the search word alphabetically
		return binary_search(word, words, high, mid+1) # search in the 2nd half of the list by making the current midpoint the new lower bound
	else:
		return mid # if neither word proceded the other then they are the same and 'word' has been found at index 'mid'
	
def precedes(word1, word2):
	""" Returns true if word1 precedes word2 alphabetically, returns False if not. """	
	for c in range(len(word1)): # iterate through each character in word1 where c is the index of the current character
		if ( len(word2) >= (c + 1)): # check that word2 hasn't run out of chars
			if ( word1[c] != word2[c]): # check they are not the same character
				if ( char_to_index(word1[c]) < char_to_index(word2[c]) ): # if the current character in word1 is lower alphabetically
					return True # word1 is lower alphabetically
				else:
					return False # word2 is lower alphabetically
		else:
			return False # word2 is lower alphabetically
	# This point will be reached if word1 has run out of characters and every character in it matched word2's chars up to this length
	# eg. word1 = ab, word2 = able
	if (len(word2) > len(word1)): # if word2 still has characters left (ie. is longer)
		return True # word1 is lower alphabetically

def funnel(word1, word2):
	""" Given two strings of letters, determine whether the second can be made from the first by removing one letter. 
	The remaining letters must stay in the same order. """
	for char in range(len(word1)):
		tempword = word1[:char] + word1[char+1:] # slice up to the current index and from 1 after that up, thus removing it for tempword		
		if ( tempword == word2): # If this permutation of word1 with a letter missing matches word2
			return True 

	return False # If no permutations of word1 with a letter missing matched word2 then return False
		  			
def bonus(word):
	""" Given a string, find all words from the enable1 word list that can be made by removing one letter from the string 'word'. """
	words = [] # The list of words from the enable1 word list that can be made by removing one letter from the string 'word'
	
	for char in range(len(word)): # iterate through each character in word
		tempword = word[:char] + word[char+1:] # slice up to the current index and from 1 after that up, thus removing it for tempword		
		if ( word_exists(tempword) ): # if this word exists (ie. is in enable1)
			if (not(tempword in words)): # Check that this word has not already been appended which can happen ## eg. "dragoon" -> "dragon"
				words.append(tempword) # add it to the list

	return words
	
while True:
	print("Funnel:")
	print("Input first word:")
	word1 = input()
	print("Input second word:")
	word2 = input()
	print(funnel(word1,word2),"\n")
	print("Press 'q' to quit, any other key to continue")
	if( input() == 'q'):
		print()
		break
		
		
while True:
	print("Bonus:")
	print("Input a word:")
	word = input()
	print(bonus(word))
	print("\nPress 'q' to quit, any other key to continue")
	if( input() == 'q'):
		break		
		
