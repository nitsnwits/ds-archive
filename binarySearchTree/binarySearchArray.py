# Binary search array implementation

from time import time

def contains(collection, target):
	"""
	define contains to use pythons 'in' operator and evaluate it's performance
	'in' generally does a sequential search, worst case O(n), best case O(1), average O(n)
	"""
	return target in collection

def binaryArraySearch(low, high, orderedCollection, target):
	"""abstract low mid stuff to allow for recursion"""
	while low <= high:
		mid = (low + high)/2
		if target == orderedCollection[mid]:
			return True
		elif target < orderedCollection[mid]:
			high = mid - 1
			return binaryArraySearch(low, high, orderedCollection, target)
		else:
			low = mid + 1
			return binaryArraySearch(low, high, orderedCollection, target)
	return False

def bsWithRecursion(orderedCollection, target):
	"""
	implement binary search to replace contains
	"""
	low = 0
	high = len(orderedCollection) - 1
	return binaryArraySearch(low, high, orderedCollection, target)

def bs_contains(orderedCollection, target):
	"""
	implement binary search without recursion
	"""
	low = 0
	high = len(orderedCollection)-1
	while low <= high:
		mid = (low + high)/2
		if target == orderedCollection[mid]:
			return mid
		elif target < orderedCollection[mid]:
			high = mid -1
		else:
			low = mid + 1
	return -(low + 1)

def insertInPlace(orderedCollection, target):
	""" insert in place using binary serach """
	index = bs_contains(orderedCollection, target)
	if index < 0:
		orderedCollection.insert(-(index + 1), target)
	


def performanceOfIn():
	"""load test contains and check performance"""
	n = 1024
	while n < 50000000:
		sortedList = range(n)
		now = time()

		# run contains with worst case scenario
		# contains(sortedList, -1)
		# bs_contains(sortedList, n + 1)
		insertInPlace(sortedList, n + 1)

		done = time()
		print n, (done - now)*10000 # show time in miliseconds

		n *= 2

def main():
	performanceOfIn()

if __name__ == '__main__':
	main()
	
