
def jDelta(numsList, diff):
	""" returns number of pairs"""
	numOfPairs = 0
	for i in range(len(numsList)):
		if find(numsList[i] + diff, numsList[i + 1:]) > 0:
			numOfPairs += 1
	return numOfPairs


def find(num, numList):
	""" use binary search to find a number in a list """
	low = 0
	high = len(numList)-1
	while low <= high:
		mid = (low + high)/2
		if num == numList[mid]:
			return mid
		elif num < numList[mid]:
			high = mid -1
		else:
			low = mid + 1
	return -(low + 1)	



def main():
	count = raw_input().split(' ')
	diff = int(count[1])
	nums = raw_input().split(' ')
	nums = map(int, nums)
	nums.sort()
	print jDelta(nums, diff)


if __name__ == '__main__':
	main()
