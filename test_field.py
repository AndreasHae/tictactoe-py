import unittest
from field import Field

class FieldTest(unittest.TestCase):

    def setUp(self):
        self.field = Field()

    def test_place(self):
        player = 'X'

        self.field.place(0, 0, player)
        cell = self.field.get(0, 0)

        self.assertEqual(player, cell)

    def test_get_winner_horiz(self):
        winner = 'X'

        for row in range(3):
            self.field.place(row, 0, winner)

        self.assertEqual(winner, self.field.get_winner())

    def test_get_winner_vert(self):
        winner = 'X'

        for col in range(3):
            self.field.place(0, col, winner)

        self.assertEqual(winner, self.field.get_winner())

    def test_get_winner_diag_from_top_left(self):
        winner = 'X'

        for i in range(3):
            self.field.place(i, i, winner)

        self.assertEqual(winner, self.field.get_winner())

    def test_get_winner_diag_from_bot_left(self):
        winner = 'X'

        self.field.place(2, 0, winner)
        self.field.place(1, 1, winner)
        self.field.place(0, 2, winner)

        self.assertEqual(winner, self.field.get_winner())
