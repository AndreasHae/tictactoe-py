class Field:
    def __init__(self):
        self.field = [[None for _ in range(3)] for _ in range(3)]

    def get(self, row, col):
        return self.field[row][col]

    def place(self, row, col, player):
        assert self.field[row][col] is not None, "Cell is not empty"

        self.field[row][col] = player

    def get_winner(self):
        # Check rows
        for row in self.field:
            if all(cell == row[0] for cell in row) and row[0] is not None:
                return row[0]

        # Check cols
        transposed_field = [list(i) for i in zip(*self.field)]
        for col in transposed_field:
            if all(cell == col[0] for cell in col) and col[0] is not None:
                return col[0]

        # Check diagonally
        player = self.field[1][1]
        if (all(cell == player for cell in [self.field[0][0], self.field[2][2]])
         or all(cell == player for cell in [self.field[2][0], self.field[0][2]])):
            return player

        return None