import unittest

from hexapawn import HexapawnGame, HexapawnException, EMPTY, WHITE, BLACK


def create_test_get_move(test_moves):
    index = 0

    def get_next_move(board, current_pawn):
        nonlocal index
        move = test_moves[index]
        index += 1
        return move

    return get_next_move


class TestHexapawnGame(unittest.TestCase):
    def test_white_reaches_other_side_game(self):
        get_white_move = create_test_get_move(
            [(2, 0, 1, 0), (2, 2, 1, 1), (1, 1, 0, 1)]
        )
        get_black_move = create_test_get_move([(0, 1, 1, 1), (0, 2, 1, 2)])

        game = HexapawnGame(
            get_white_move=get_white_move, get_black_move=get_black_move
        )
        game.next_move()
        game.next_move()
        game.next_move()
        game.next_move()
        winner, _, _ = game.next_move()

        self.assertEqual(winner, WHITE)

    def test_black_reaches_other_side_game(self):
        get_white_move = create_test_get_move([(2, 0, 1, 0), (2, 1, 1, 1)])
        get_black_move = create_test_get_move([(0, 1, 1, 0), (1, 0, 2, 0)])

        game = HexapawnGame(
            get_white_move=get_white_move, get_black_move=get_black_move
        )
        game.next_move()
        game.next_move()
        game.next_move()
        winner, _, _ = game.next_move()

        self.assertEqual(winner, BLACK)

    def test_white_runs_out_of_moves(self):
        get_white_move = create_test_get_move([(2, 0, 1, 0), (2, 2, 1, 1)])
        get_black_move = create_test_get_move([(0, 1, 1, 1), (0, 2, 1, 1)])

        game = HexapawnGame(
            get_white_move=get_white_move, get_black_move=get_black_move
        )
        game.next_move()
        game.next_move()
        game.next_move()
        game.next_move()
        winner, _, _ = game.next_move()

        self.assertEqual(winner, BLACK)

    def test_black_runs_out_of_moves(self):
        get_white_move = create_test_get_move(
            [(2, 1, 1, 1), (2, 2, 1, 1), (2, 0, 1, 1)]
        )
        get_black_move = create_test_get_move([(0, 2, 1, 1), (0, 0, 1, 1)])

        game = HexapawnGame(
            get_white_move=get_white_move, get_black_move=get_black_move
        )
        game.next_move()
        game.next_move()
        game.next_move()
        game.next_move()
        game.next_move()
        winner, _, _ = game.next_move()

        self.assertEqual(winner, WHITE)
