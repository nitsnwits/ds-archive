# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. Do this without extra space.
# click to show spoilers.
# Some hints:
# Could negative integer be palindromes? (ie, -1)
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# There is a more generic way of solving this problem.


class Solution:
	# @param {integer} x
	# @return {boolean}
	def isPalindromeOld(self, x):
		if x < 0:
			return False
		end = self.lenOfInt(x) - 1
		if end % 2 == 0:
			ren = end/2
		else:
			ren = end/2 + 1
		for i in range(ren):
			if x%10 == x/10**end:
				x = x/10
				x = x/10**end
				end -=1
			else:
				return False
		return True

	def lenOfInt(self, x = None):
		if x is None or type(x) == 'str':
			return 0
		len = 0
		while x != 0:
			len += 1
			x = x/10
		return len

	def isPalindrome(self, x):
		if x < 0:
			return False
		p1 = 0
		p2 = x
		while (p2 > 0):
			p1 = p1*10 + p2%10
			p2 /= 10
		return p1 == x



import unittest
class TestSolution(unittest.TestCase):
	def testInit(self):
		isPal = Solution()
		self.assertTrue(isPal.isPalindrome(12321))
		self.assertFalse(isPal.isPalindrome(10))

	def testNegative(self):
		isPal = Solution()
		self.assertFalse(isPal.isPalindrome(-12321))

	def testLenOfInt(self):
		isPal = Solution()
		self.assertEqual(isPal.lenOfInt(54321), 5)
		self.assertEqual(isPal.lenOfInt(1),1)
		self.assertEqual(isPal.lenOfInt(), 0)

	def testEvens(self):
		isPal = Solution()
		self.assertTrue(isPal.isPalindrome(123456789987654321))
		self.assertTrue(isPal.isPalindrome(11))
		self.assertTrue(isPal.isPalindrome(2222))
		self.assertTrue(isPal.isPalindrome(100001))

	def testOdds(self):
		isPal = Solution()
		self.assertTrue(isPal.isPalindrome(12345678987654321))
		self.assertTrue(isPal.isPalindrome(111))
		self.assertTrue(isPal.isPalindrome(22222))
		self.assertTrue(isPal.isPalindrome(10001))
	
	def testLeetEdgeCases(self):
		isPal = Solution()
		self.assertFalse(isPal.isPalindrome(100021))

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

