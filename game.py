from field import Field

def player_generator():
    while True:
        yield 'X'
        yield 'O'

player = player_generator()

class TicTacToe:

    def __init__(self):
        self.__player_gen = player_generator()
        self.__field = Field()

    def turn(self, row, col):
        assert row < 3 and row >= 0
        assert col < 3 and col >= 0
        assert self.__field.get(row, col) == None

        self.__field.place(row, col, next(self.__player_gen))

    def get_winner(self):
        return self.__field.get_winner()
