pawn_move_list = [[0,1],[0,-1]]

black_pawn_attack_move_list = [[-1,-1],[1,-1]]

white_pawn_attack_move_list = [[1,1],[-1,1]]

rook_move_list = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
					[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],
					[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
					[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]]

knight_move_list = [[1,2],[1,-2],[-1,2],[-1,-2],[2, 1],[2,-1],[-2,1],[-2,-1]]

bishop_move_list = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],
						[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],
						[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],
						[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]]

queen_move_list = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
					[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],
					[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
					[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],
					[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],
					[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],
					[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],
					[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]]

king_move_list = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]


class Piece:
	def __init__(self, name, type, color):
		self.name = name
		self.type = type
		self.color = color
		self.has_moved = False
		self.pawn_attack = False


	def Move(self, x, y):
		if self.type == "Pawn":
			move = [x, y]
			if self.name == "wP" and move == [0, 1] or self.name == "bP" and move == [0, -1] \
				or not self.has_moved and self.name == "wP" and move == [0, 2] \
				or not self.has_moved and self.name == "bP" and move == [0, -2]:
				if not self.has_moved:
					self.has_moved = True
				return True
			elif self.name == "wP" and self.pawn_attack == True:
				for moves in white_pawn_attack_move_list:
					if move == moves:
						if not self.has_moved:
							self.has_moved = True
						self.pawn_attack = False
						return True
			elif self.name == "bP" and self.pawn_attack == True:
				for moves in black_pawn_attack_move_list:
					if move == moves:
						if not self.has_moved:
							self.has_moved = True
						self.pawn_attack = False
						return True
			else:
				self.pawn_attack = False
				return False

		elif self.type == "Rook":
			move = [y, x]
			for moves in rook_move_list:
				if move == moves:
					if not self.has_moved:
						self.has_moved = True
					return True
			else:
				return False

		elif self.type == "Knight":
			move = [y,x]
			for moves in knight_move_list:
				if move == moves:
					if not self.has_moved:
						self.has_moved = True
					return True
			else:
				return False

		elif self.type == "Bishop":
			move = [y, x]
			for moves in bishop_move_list:
				if move == moves:
					if not self.has_moved:
						self.has_moved = True
					return True
			else:
				return False

		elif self.type == "Queen":
			move = [y, x]
			for moves in rook_move_list:
				if move == moves:
					if not self.has_moved:
						self.has_moved = True
					return True
			else:
				return False

		elif self.type == "King":
			move = [y, x]
			for moves in rook_move_list:
				if move == moves:
					if not self.has_moved:
						self.has_moved = True
					return True
			else:
				return False

		else:
			return False

