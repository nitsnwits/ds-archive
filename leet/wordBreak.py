# https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".


class Solution:
	# @param s, a string
	# @param wordDict, a set<string>
	# @return a boolean
	def wordBreak(self, s, wordDict):
		temp = ''
		for i in s:
			temp += i
			if i in wordDict:
				temp = ''



import unittest
class TestSolution(unittest.TestCase):
	def testInit(self):
		s = Solution()
		self.assertTrue(s.wordBreak('leetcode', ["leet", "code"]))

testSuite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(testSuite)