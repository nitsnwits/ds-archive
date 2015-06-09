# https://leetcode.com/problems/length-of-last-word/
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.
def lengthOfLastWordSimple(s):
	stringArray = s.strip().split(' ')
	return len(stringArray[-1])

def lengthOfLastWord(s):
	ans = 0
	if len(s) == 0:
		return 0
	s = newStrip(s)
	for i in s:
		ans += 1
		if i == ' ':
			ans = 0
	return ans

def newStrip(s):
	while s[-1] == ' ' and len(s) > 1:
		s = s[:-1]
	return s

# print lengthOfLastWord('Hello World')
# print lengthOfLastWord(' ')
# print lengthOfLastWord('a ')
# print lengthOfLastWord('')
s = '.txt is a file format for files consisting of text usually containing very little formatting (e.g., no bolding or italics). The precise definition of the .txt format is not specified, but typically matches the format accepted by the system terminal or simple text editor. Files with the .txt extension can easily be read or opened by any program that reads text and, for that reason, are considered universal (or platform independent). The ASCII character set is the most common format for English-language text files, and is generally assumed to be the default file format in many situations. For accented and other non-ASCII characters, it is necessary to choose a character encoding. In many systems, this is chosen on the basis of the default locale setting on the computer it is read on. Common character encodings include ISO 8859-1 for many European languages. Because many encodings have only a limited repertoire of characters, they are often only usable to represent text in a limited subset of human languages. Unicode is an attempt to create a common standard for representing all known languages, and most known character sets are subsets of the very large Unicode character set. Although there are multiple character encodings available for Unicode, the most common is UTF-8, which has the advantage of being backwards-compatible with ASCII; that is, every ASCII text file is also a UTF-8 text file with identical meaning. The main issue between pure ASCII and pure UTF-8 is limited to the presence or absence of the BOM. According to Microsoft, the Unicode protocol used for txt files is UTF-8, although in Notepad the encoding UTF-16LE is called Unicode.'
print lengthOfLastWord(s)