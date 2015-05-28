"""
https://www.hackerrank.com/challenges/funny-string
"""
import sys
import string

def findFunny(word):
	# use extended slices and reverse the string
	reverseWord = word[::-1]
	for i in range(1, len(word)):
		if distanceInChars(word[i-1], word[i]) != distanceInChars(reverseWord[i-1], reverseWord[i]):
			print 'Not Funny'
			return
	print 'Funny'
	return

def distanceInChars(charA, charB):
	"""
	returns int distance 
	"""
	indexOfCharA = string.ascii_lowercase.index(charA.lower())
	indexOfCharB = string.ascii_lowercase.index(charB.lower())
	return abs(indexOfCharA - indexOfCharB)

def main():
	count = input()
	for words in range(count):
		word = raw_input()
		findFunny(word)	

if __name__ == '__main__':
	main()


