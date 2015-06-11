# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
	# constructor
	def __init__(self):
		self.stack = []
		# reverse sorted stack, e.g. 5,4,3,2,1 (getMin is top of minStack)
		self.minStack = []

	# @param x, an integer
	# @return an integer
	def push(self, x):
		self.stack.append(x)
		self.insertInPlace(x)
		return x

	# @return nothing
	def pop(self):
		elem = self.stack.pop()
		self.minStack.remove(elem)
		return None

	# @return an integer
	def top(self):
		if len(self.stack) > 0:
			return self.stack[-1]
		else:
			return None

	# @return an integer
	def getMin(self):
		if len(self.minStack) > 0:
			return self.minStack[0]
		else:
			return None

	def findInsertPosition(self, x):
		""" binary serach array impl for minstack """
		low = 0
		high = len(self.minStack) - 1
		mid = None
		while low <= high:
			mid = (low + high)/2
			if self.minStack[mid] == x:
				return mid + 1
			elif self.minStack[mid] < mid:
				high = mid - 1
			else:
				low = mid + 1
		return -(low + 1)

	def insertInPlace(self, x):
		pos = self.findInsertPosition(x)
		if pos < 0:
			self.minStack.insert(-(pos + 1), x)
			return None
		self.minStack.insert(pos, x)
		return None
		

	def getMinStack(self):
		return self.minStack


import unittest
class TestMinStack(unittest.TestCase):
	def testTreeInit(self):
		st = MinStack()
		st.push(5)
		self.assertEqual(st.top(), 5)
		st.push(6)
		self.assertEqual(st.top(), 6)
		self.assertEqual(st.getMin(), 5)
		st.pop()
		self.assertEqual(st.getMin(), 5)

	def testEdgeCase(self):
		st = MinStack()
		st.push(0)
		st.push(1)
		st.push(0)
		self.assertEqual(st.top(), 0)
		self.assertEqual(st.getMin(), 0)
		st.pop()
		self.assertEqual(st.top(), 1)
		self.assertEqual(st.getMin(),0)
		print st.getMinStack()

	def testLoad(self):
		st = MinStack()
		for i in range(-1000, 0):
			st.push(i)
   

suite = unittest.TestLoader().loadTestsFromTestCase(TestMinStack)
unittest.TextTestRunner(verbosity=2).run(suite)