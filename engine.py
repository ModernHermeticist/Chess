from board import Board
from gamestates import GameStates


def main():
	gamestate = GameStates.BLACK_PLAYER_TURN
	next_gamestate = GameStates.WHITE_PLAYER_TURN
	canMovePiece = True
	b = Board()
	b.InitBoard()
	b.playerOne = chooseColor()
	if b.playerOne == "white":
		b.playerTwo = "black"
	else:
		b.playerTwo = "white"

	while True:
		b.PrintBoard(gamestate)
		
		if b.checkKing(gamestate):
			if gamestate == GameStates.BLACK_PLAYER_TURN:
				if b.checkWhite == True:
					print("Black wins!")
					break
				b.checkWhite = True
			elif gamestate == GameStates.WHITE_PLAYER_TURN:
				if b.checkBlack == True:
					print("White wins!")
					break
				b.checkBlack = True
		else:
			if gamestate == GameStates.BLACK_PLAYER_TURN:
				b.checkWhite = False
			elif gamestate == GameStates.WHITE_PLAYER_TURN:
				b.checkBlack = False

		if not canMovePiece:
			print("Enter a valid move for the piece!")
		x_1, y_1, x_2, y_2 = b.getInput(gamestate)
		if not b.MovePiece(x_1, y_1, x_2, y_2):
			canMovePiece = False
			continue
		else:
			canMovePiece = True

			if gamestate == GameStates.BLACK_PLAYER_TURN:
				gamestate = GameStates.WHITE_PLAYER_TURN
			elif gamestate == GameStates.WHITE_PLAYER_TURN:
				gamestate = GameStates.BLACK_PLAYER_TURN


def chooseColor():
	while True:
		color = input("Please enter your color, either white or black: ")
		color = color.lower()
		if color != "white" and color != "black":
			continue
		else:
			break
	return color



if __name__ == "__main__":
	main()