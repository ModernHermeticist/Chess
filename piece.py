pawn_move_list = [[0,1],[0,-1]] #temporary testing move list
rook_move_list = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
					[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],
					[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
					[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]]


class Piece:
	def __init__(self, name, type, color):
		self.name = name
		self.type = type
		self.color = color
		self.has_moved = False


	def Move(self, x, y):
		if self.type == "Pawn":
			move = [y, x]
			if self.name == "wP" and move == [0, 1] or self.name == "bP" and move == [0, -1] \
				or not self.has_moved and self.name == "wP" and move == [0, 2] \
				or not self.has_moved and self.name == "bP" and move == [0, -2]:
				if not self.has_moved:
					self.has_moved = True
				return True
			else:
				print("Whoops")
				return False

		if self.type == "Rook":
			move = [y, x]
			for moves in rook_move_list:
				if move == moves:
					if not self.has_moved:
						self.has_moved = True
					return True
			else:
				print("Whoops")
				return False

		else:
			print("Whoops")
			return False

