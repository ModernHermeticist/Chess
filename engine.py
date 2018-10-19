from board import Board



def main():
	b = Board()
	b.InitBoard()
	while True:
		b.PrintBoard()
		x_1, y_1, x_2, y_2 = getInput()
		b.MovePiece(x_1, y_1, x_2, y_2)


def getInput():
	x_1, y_1 = input("Enter piece x,y coordinate: ").split()
	x_2, y_2 = input("Enter x,y coordinate to move: ").split()

	return int(x_1), int(y_1), int(x_2), int(y_2)





if __name__ == "__main__":
	main()