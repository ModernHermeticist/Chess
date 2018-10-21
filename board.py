from piece import Piece
from gamestates import GameStates


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
		self.playerOne = ""
		self.playerTwo = ""
		self.checkWhite = False
		self.checkBlack = False


	def InitBoard(self):
		for i in range(0,2):
			for j in range(0,8):
				white_piece_id = piece_ID[i][j]
				black_piece_id = piece_ID[1-i][j]
				wp = Piece(white_pieces_names[i][j], white_piece_id, "white")
				bp = Piece(black_pieces_names[i][j], black_piece_id, "black")
				self.board[i][j] = wp
				self.board[i+6][j] = bp

	def PrintBoard(self, gamestate):
		print("\n")
		if gamestate == GameStates.WHITE_PLAYER_TURN:
			print("White's turn!\n")
			if self.checkWhite:
				print("White is in check!")
		elif gamestate == GameStates.BLACK_PLAYER_TURN:
			print("Black's turn!\n")
			if self.checkBlack:
				print("Black is in check!")
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
		Blocked = self.Blocked(x_1, y_1, x_2, y_2)
		if p.type == "Knight":
			Blocked = False
		Friendly_At_Destination = self.Friendly(x_1, y_1, x_2, y_2)
		canMovePiece = p.Move(movex, movey)
		if not canMovePiece:
			return False
		if not Friendly_At_Destination and not Blocked:
			self.board[y_1][x_1] = 0
			self.board[y_2][x_2] = p
			return True

	def Blocked(self, x_1, y_1, x_2, y_2):
		movex = x_2 - x_1
		movey = y_2 - y_1


		if movey == 0:
			if x_2 > x_1:
				for i in range(x_1+1, x_2):
					if self.board[y_1+movey][i] != 0:
						return True
				else:
					return False

			elif x_1 > x_2:
				for i in range(x_2, x_1):
					if self.board[y_1+movey][i] != 0:
						return True
				else:
					return False

		elif movex == 0:
			if y_2 > y_1:
				for i in range(y_1+1, y_2):
					if self.board[i][x_1+movex] != 0:
						return True
				else:
					return False

			elif y_1 > y_2:
				for i in range(y_2, y_1):
					if self.board[i][x_1+movex] != 0:
						return True
				else:
					return False

		else:
			if movex == movey:
				if y_1 > y_2 and x_1 > x_2:
					j = 0
					for i in range(y_2, y_1):
						if self.board[i][j] != 0:
							return True
						j += 1
					else:
						return False
				elif y_2 > y_1 and x_2 > x_1:
					j = 1
					for i in range(y_1+1, y_2):
						if self.board[i][j] != 0:
							return True
						j += 1
					else:
						return False

			elif movex == -movey:
				if y_1 > y_2 and x_1 > x_2:
					j = 0
					for i in range(y_2, y_1):
						if self.board[i][j]:
							return True
					else:
						return False
				elif y_2 > y_1 and x_2 > x_1:
					j = 1
					for i in range(y_1+1, y_2):
						if self.board[i][j]:
							return True
					else:
						return False
			else:
				return False

	def Friendly(self, x_1, y_1, x_2, y_2):

		try:
			color = self.board[y_2][x_2].color
		except:
			return False

		if self.board[y_1][x_1].color != self.board[y_2][x_2].color:
			return False
		else:
			return True

	def getInput(self, gamestate):
		while True:
			try:
				x_1, y_1 = input("Enter piece x, y coordinates: ").split()
			except(ValueError):
				print("Please enter a valid set of coordinates.")
				continue
			x_1 = int(x_1)
			y_1 = int(y_1)
			try:
				s = self.board[y_1][x_1]
				if s == 0:
					print("Please enter a valid set of coordinates.")
					continue
				if gamestate == GameStates.WHITE_PLAYER_TURN and s.color != "white":
					print("Please enter a valid set of coordinates.")
					continue
				if gamestate == GameStates.BLACK_PLAYER_TURN and s.color != "black":
					print("Please enter a valid set of coordinates.")
					continue

			except (IndexError):
				print("Please enter a valid set of coordinates.")
				continue
			else:
				break
		while True:
			try:
				x_2, y_2 = input("Enter x, y coordinates to move: ").split()
			except(ValueError):
				print("Please enter a valid set of coordinates.")
				continue
			x_2 = int(x_2)
			y_2 = int(y_2)
			try:
				t = self.board[y_2][x_2]

				if t != 0 and gamestate == GameStates.WHITE_PLAYER_TURN and t.color == "white":
					print("Please enter a valid set of coordinates.")
					continue
				if t != 0 and gamestate == GameStates.BLACK_PLAYER_TURN and t.color == "black":
					print("Please enter a valid set of coordinates.")
					continue
				if s.type == "Pawn" and t == 0:
					s.pawn_attack = False
					if abs(x_2 - x_1) != 0:
						print("Please enter a valid set of coordinates.")
						continue
				elif s.type == "Pawn" and t != 0:
					s.pawn_attack = True

			except (IndexError):
				print("Please enter a valid set of coordinates.")
				continue
			else:
				break

		return x_1, y_1, x_2, y_2

	def checkKing(self, gamestate):
		k = ""
		x_k = 0
		y_k = 0
		if gamestate == GameStates.BLACK_PLAYER_TURN:
			for i in range(0,self.height):
				for j in range(0,self.width):
					n = self.board[i][j]
					if n == 0:
						continue
					elif n.name == "wK":
						k = self.board[i][j]
						x_k = j
						y_k = i
						break
				if k == "wK":
					break
		elif gamestate == GameStates.WHITE_PLAYER_TURN:
			for i in range(0,self.height):
				for j in range(0,self.width):
					n = self.board[i][j]
					if n == 0:
						continue
					elif n.name == "bK":
						k = self.board[i][j]
						x_k = j
						y_k = i
						break
				if k == "bK":
					break

		if gamestate == GameStates.BLACK_PLAYER_TURN:
			for i in range(0,self.height):
				for j in range(0,self.width):
					t = self.board[i][j]
					if t == 0:
						continue
					else:
						movex = x_k - j
						movey = y_k - i
						Blocked = self.Blocked(j, i, x_k, y_k)
						print("test")
						if t.type == "Knight":
							Blocked = False
							print("test1")
							print("self.board[i][j].color: {0}".format(self.board[i][j].color))
							print("k.Move(movex, movey): {0}".format(k.Move(movex, movey)))
							print("Blocked: {0}".format(Blocked))
						if self.board[i][j].color == "black" and (t.Move(movex, movey) and not Blocked):
							print("test2")
							return True
			else:
				return False

		elif gamestate == GameStates.WHITE_PLAYER_TURN:
			for i in range(0,self.height):
				for j in range(0,self.width):
					t = self.board[i][j]
					if t == 0:
						continue
					else:
						movex = x_k - j
						movey = y_k - i
						Blocked = self.Blocked(j, i, x_k, y_k)
						if t.type == "Knight":
							Blocked = False
						if self.board[i][j].color == "white" and (t.Move(movex, movey) and not Blocked):
							return True
			else:
				return False
