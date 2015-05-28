"""
https://www.hackerrank.com/challenges/two-strings
"""
import sys
import string

def findCommonSubstrings(firstWord, secondWord):
	comparisonDict = {}
	for i in firstWord:
		comparisonDict[i] = 0
	for i in secondWord:
		if i in comparisonDict:
			print 'YES'
			return
	print 'NO'
	return


def main():
	count = input()
	for i in range(count):
		firstWord = raw_input()
		secondWord = raw_input()
		findCommonSubstrings(firstWord, secondWord)

if __name__ == '__main__':
	main()


