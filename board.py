from piece import Piece


white_pieces_names = [['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
						['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']]

black_pieces_names = [['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
						['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']]

piece_ID      	   = [['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook'],
					  ['Pawn', 'Pawn',   'Pawn',   'Pawn',  'Pawn', 'Pawn',   'Pawn',   'Pawn']]


class Board:
	def __init__(self, height=8, width=8):
		self.height = height
		self.width = width
		self.board = [[0] * self.width for i in range(self.height)]

	def InitBoard(self):
		for i in range(0,2):
			for j in range(0,8):
				white_piece_id = piece_ID[i][j]
				black_piece_id = piece_ID[1-i][j]
				wp = Piece(white_pieces_names[i][j], white_piece_id, "White")
				bp = Piece(black_pieces_names[i][j], black_piece_id, "Black")
				self.board[i][j] = wp
				self.board[i+6][j] = bp

	def PrintBoard(self):
		print("\n")
		for i in range(0,8):
			print("".rjust(15) + str(i) + " |", end="")
			for j in range(0,8):
				p = self.board[i][j]
				try:
					p = p.name
				except AttributeError:
					pass
				print("" + str(p).rjust(4), end="")
			if(i == 7):
				print("")
			else:
				print("\n")
		print("".rjust(20) + "------------------------------")
		print("".rjust(20), end="")
		for i in range(0, 8):
			print(" " + str(i) + "".rjust(2), end="")
		print("\n")

	def MovePiece(self, x_1, y_1, x_2, y_2):
		movex = x_2 - x_1
		movey = y_2 - y_1
		p = self.board[y_1][x_1]
		is_Blocked = self.Blocked(x_1, y_1, x_2, y_2)
		is_Friendly = self.is_Friendly(x_1, y_1, x_2, y_2)
		if(not is_Blocked and p.Move(movey, movex)):
			self.board[y_1][x_1] = 0
			self.board[y_2][x_2] = p
		elif(is_Blocked and not is_Friendly):
			self.board[y_1][x_1] = 0
			self.board[y_2][x_2] = p

	def Blocked(self, x_1, y_1, x_2, y_2):
		movex = x_2 - x_1
		movey = y_2 - y_1

		if movex >= 0 and movey >= 0:
			for i in range(0, movex+1):
				for j in range(0, movey+1):
					if self.board[i][j].type != None:
						return True
			else:
				return False

		if movex >= 0 and movey < 0:
			for i in range(0, movex+1):
				for j in range(movey, 1):
					if self.board[i][j].type != None:
						return True
			else:
				return False

		if movex < 0 and movey >= 0:
			for i in range(movex, 1):
				for j in range(0, movey+1):
					if self.board[i][j].type != None:
						return True
			else:
				return False

		if movex < 0 and movey < 0:
			for i in range(movex, 1):
				for j in range(movey, 1):
					if self.board[i][j].type != None:
						return True
			else:
				return False

	def is_Friendly(self, x_1, y_1, x_2, y_2):

		try:
			color = self.board[y_2][x_2].color
		except:
			return False

		if self.board[y_1][x_1].color != self.board[y_2][x_2].color:
			return False
		else:
			return True
