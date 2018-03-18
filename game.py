from field import Field

def player_generator():
    while True:
        yield 'X'
        yield 'O'

class Game:

    def __init__(self):
        self.__player_gen = player_generator()
        self.__next_player = next(self.__player_gen)
        self.__field = Field()

    def turn(self, row, col):
        assert row < 3 and row >= 0
        assert col < 3 and col >= 0
        assert self.__field.get(row, col) == None

        self.__field.place(row, col, self.__next_player)
        self.__next_player = next(self.__player_gen)

    @property
    def winner(self):
        return self.__field.get_winner()

    @property
    def next_player(self):
        return self.__next_player
