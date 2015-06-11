# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Credits:
# Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
    	iteration = 0
        while n > 3:
        	idx = n
        	interim = 0
        	while idx > 0:
        		interim += (idx%10)**2
        		idx = idx/10
        	n = interim
        	iteration += 1
        	if iteration > 10:
        		return False
    	if n == 1:
    		return True
    	return False


import unittest
class TestIsHappy(unittest.TestCase):
	def testInit(self):
		n = Solution()
		self.assertTrue(n.isHappy(19))

	def testTrue(self):
		n = Solution()
		self.assertTrue(n.isHappy(1))
		self.assertTrue(n.isHappy(7))

	def testFalse(self):
		n = Solution()
		self.assertFalse(n.isHappy(5))
		self.assertFalse(n.isHappy(18))


testSuite = unittest.TestLoader().loadTestsFromTestCase(TestIsHappy)
unittest.TextTestRunner(verbosity=2).run(testSuite)