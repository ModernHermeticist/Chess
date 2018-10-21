from enum import Enum

class GameStates(Enum):
	BLACK_PLAYER_TURN = 1
	WHITE_PLAYER_TURN = 2
	BLACK_PLAYER_WIN  = 3
	WHITE_PLAYER_WIN  = 4