import unittest

from hexapawn import HexapawnBoard, HexapawnException, EMPTY, WHITE, BLACK


class TestHexapawnBoard(unittest.TestCase):
    def test_move_white_pawn(self):
        board = HexapawnBoard()
        board.move_pawn(2, 0, 1, 0)
        self.assertEqual(board.get_pawn(2, 0), EMPTY)
        self.assertEqual(board.get_pawn(1, 0), WHITE)

    def test_move_black_pawn(self):
        board = HexapawnBoard()
        board.move_pawn(0, 0, 1, 0)
        self.assertEqual(board.get_pawn(0, 0), EMPTY)
        self.assertEqual(board.get_pawn(1, 0), BLACK)

    def test_cannot_move_forward_when_blocked(self):
        board = HexapawnBoard()
        board.move_pawn(0, 0, 1, 0)
        with self.assertRaises(HexapawnException):
            board.move_pawn(1, 0, 2, 0)

    def test_black_attack_white(self):
        board = HexapawnBoard()
        board.move_pawn(0, 0, 1, 0)
        board.move_pawn(1, 0, 2, 1)
        self.assertEqual(board.get_pawn(0, 0), EMPTY)
        self.assertEqual(board.get_pawn(1, 0), EMPTY)
        self.assertEqual(board.get_pawn(2, 1), BLACK)

    def test_white_attack_black(self):
        board = HexapawnBoard()
        board.move_pawn(2, 1, 1, 1)
        board.move_pawn(1, 1, 0, 0)
        self.assertEqual(board.get_pawn(2, 1), EMPTY)
        self.assertEqual(board.get_pawn(1, 1), EMPTY)
        self.assertEqual(board.get_pawn(0, 0), WHITE)

    def test_no_valid_moves_white(self):
        board = HexapawnBoard(
            [EMPTY, EMPTY, EMPTY, EMPTY, BLACK, EMPTY, EMPTY, WHITE, EMPTY]
        )
        self.assertFalse(board.has_legal_move(WHITE))

    def test_no_valid_moves_black(self):
        board = HexapawnBoard(
            [EMPTY, BLACK, EMPTY, EMPTY, WHITE, EMPTY, EMPTY, EMPTY, EMPTY]
        )
        self.assertFalse(board.has_legal_move(WHITE))

    def test_white_reached_other_side(self):
        board = HexapawnBoard(
            [EMPTY, WHITE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        )
        self.assertTrue(board.has_reached_other_side(WHITE))

    def test_black_reached_other_side(self):
        board = HexapawnBoard(
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLACK, EMPTY]
        )
        self.assertTrue(board.has_reached_other_side(BLACK))

    def test_neither_reached_other_side(self):
        board = HexapawnBoard()
        self.assertFalse(board.has_reached_other_side(WHITE))
        self.assertFalse(board.has_reached_other_side(BLACK))
