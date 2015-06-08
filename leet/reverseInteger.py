# https://leetcode.com/problems/reverse-integer/
# reverse an reverse-integer
# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

def reverse(num):
	digits = 0
	flag = False
	if num < 0:
		flag = True
		num = abs(num)
	iterateNum = num
	# increases complexity of O(n), number of digits = int(math.log10(n)) + 1 is another way
	while iterateNum != 0:
		iterateNum /= 10
		digits += 1

	finalNum = 0
	reverseTraverse = digits - 1
	for i in range(1, digits+1):
		lastDigit = num%10
		num /= 10
		finalNum = finalNum + lastDigit*10**reverseTraverse
		reverseTraverse -= 1
	if flag:
		return -1*finalNum
	if finalNum > 2147483647:
		return 0
	return finalNum
	

print reverse(123)
print reverse(-123)
print reverse(10000000)
print reverse(123456789)
