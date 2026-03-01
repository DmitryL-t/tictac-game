class Board:
	def __init__(self, b=None, move='x'):
		if b == None:
			b = [[None] * 3 for i in range(3)]
		self.b = b
		self.move = move
	def possible_moves(self):
		l = []
		for i in range(3):
			for j in range(3):
				if self.b[i][j] == None:
					l.append((i, j))
		return l
	def get_c(self, p, p1=0):
		if type(p) == tuple:
			(a, b) = p
		else:
			a, b = p // 3, p % 3
		return self.b[a][b]
	def result(self):
		h = [
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6)
		]
		for i in h:
			if self.get_c(i[0]) == self.get_c(i[1]) == self.get_c(i[2]) != None:
				return self.get_c(i[0])
		count = 0
		for i in range(3):
			for j in range(3):
				if self.b[i][j] != None:
					count += 1
		if count == 9:
			return 'draw'
		return False
	def score(self):
		res = self.result()
		if res == 'x':
			return (1, 0)
		elif res == 'o':
			return (0, 1)
		elif res == 'draw':
			return (1 / 2, 1 / 2)
		return None
	def move_(self, p):
		(a, b) = p
		self.b[a][b] = self.move
		if self.move == 'x':
			self.move = 'o'
		else:
			self.move = 'x'
	def move_new_board(self, p):
		board = Board(self.b, self.move)
		board.move_(p)
		return board

board = Board()
while not board.result():
	print(board.b)
	board.move_(board.possible_moves()[0])
print(board.b)
