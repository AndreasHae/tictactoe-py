import unittest
from game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_next_player(self):
        first_player = self.game.next_player
        self.game.turn(0, 0)

        second_player = self.game.next_player
        self.game.turn(1, 0)

        self.assertEqual(first_player, self.game.next_player)
        self.game.turn(0, 1)

        self.assertEqual(second_player, self.game.next_player)

    def test_turn_input_checked(self):
        with self.assertRaises(AssertionError):
            self.game.turn(-1, -1)

        with self.assertRaises(AssertionError):
            self.game.turn(3, 3)

    def test_turn_cell_occupied(self):
        self.game.turn(0, 0)
        with self.assertRaises(AssertionError):
            self.game.turn(0, 0)
