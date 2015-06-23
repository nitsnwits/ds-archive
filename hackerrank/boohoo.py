
def boohoo(num):
	for i in range(1, num+1):
		if (i%3 == 0 and i%5==0):
			print 'BooHoo'
		elif (i%3 == 0):
			print 'Boo'
		elif (i%5 == 0):
			print 'Hoo'
		else:
			print i



def main():
	number = input()
	boohoo(number)

if __name__ == '__main__':
	main()