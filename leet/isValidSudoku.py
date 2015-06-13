# https://leetcode.com/problems/valid-sudoku/
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution:
	# @param {character[][]} board
	# @return {boolean}
	def isValidSudoku(self, board):
		# check rows and columns
		for i in range(len(board)):
			for j in range(len(board)):
				if self.checkDuplicatesInAnArray(board[i][j]):
					return False
		# check squares
		numberOfSquaresInOneRow = len(board)/3
		start = 0
		for i in range(numberOfSquaresInOneRow):
			square = (range(start, start + 3))
			squareList = []
			for i in square:
				for j in square:
					if board[i][j] != '.':
						squareList.append(board[i][j])
			if self.checkDuplicatesInAnArray(squareList):
				return False
			start += 3
		return True



	def checkDuplicatesInAnArray(self, array):
		dupsDict = {}
		for i in array:
			if i in dupsDict:
				return True
			else:
				if i != '.':
					dupsDict[i] = 0
		return False