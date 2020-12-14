from hexapawn.HexapawnConstants import (
    EMPTY,
    BLACK,
    WHITE,
    SIZE,
    BLACK_DIRECTION,
    WHITE_DIRECTION,
)
from hexapawn.HexapawnException import HexapawnException

DEFAULT_BOARD = [
    BLACK,
    BLACK,
    BLACK,
    EMPTY,
    EMPTY,
    EMPTY,
    WHITE,
    WHITE,
    WHITE,
]


class HexapawnBoard:
    def __init__(self, initialBoard=None):
        if (
            initialBoard is not None
            and len(initialBoard) == SIZE * SIZE
            and all([state in [EMPTY, WHITE, BLACK] for state in initialBoard])
        ):
            self.board = initialBoard[:]
        else:
            self.board = DEFAULT_BOARD[:]

    def get_pawn(self, row, col):
        if row >= SIZE or col >= SIZE:
            return None
        return self.board[row * SIZE + col]

    def set_pawn(self, row, col, state):
        if state not in [EMPTY, BLACK, WHITE]:
            raise HexapawnException("Invalid board state")
        self.board[row * SIZE + col] = state

    def move_pawn(self, start_row, start_col, end_row, end_col):
        current_pawn = self.get_pawn(start_row, start_col)
        if current_pawn == EMPTY or current_pawn == None:
            raise HexapawnException("No pawn at that position")
        if end_row >= SIZE or end_col >= SIZE:
            raise HexapawnException("Cannot move pawn off the board")

        if not self._check_is_valid_move(
            start_row, start_col, end_row, end_col, current_pawn
        ):
            raise HexapawnException("Invalid move")

        self.set_pawn(start_row, start_col, EMPTY)
        self.set_pawn(end_row, end_col, current_pawn)

    def has_legal_move(self, pawn_color):
        for row in range(SIZE):
            for col in range(SIZE):
                pawn = self.get_pawn(row, col)
                if pawn == pawn_color:
                    if self._pawn_has_legal_move(row, col, pawn_color):
                        return True
        return False

    def has_reached_other_side(self, pawn_color):
        direction = WHITE_DIRECTION if pawn_color == WHITE else BLACK_DIRECTION
        if direction < 0:
            for col in range(SIZE):
                if self.get_pawn(0, col) == pawn_color:
                    return True
        else:
            for col in range(SIZE):
                if self.get_pawn(SIZE - 1, col) == pawn_color:
                    return True
        return False

    def _pawn_has_legal_move(self, row, col, pawn_color):
        if pawn_color == WHITE:
            target_row = row + WHITE_DIRECTION
        else:
            target_row = row + BLACK_DIRECTION
        if self._check_is_valid_move(row, col, target_row, col, pawn_color):
            return True
        if col - 1 >= 0 and self._check_is_valid_move(
            row, col, target_row, col - 1, pawn_color
        ):
            return True
        if col + 1 < SIZE and self._check_is_valid_move(
            row, col, target_row, col + 1, pawn_color
        ):
            return True
        return False

    def check_is_valid_move(self, start_row, start_col, end_row, end_col, pawn_color):
        current_pawn = self.get_pawn(start_row, start_col)
        if current_pawn == EMPTY or current_pawn == None:
            return False
        if end_row >= SIZE or end_col >= SIZE:
            return False
        return self._check_is_valid_move(
            start_row, start_col, end_row, end_col, current_pawn
        )

    def _check_is_valid_move(self, start_row, start_col, end_row, end_col, pawn_color):
        return self._check_is_valid_normal_move(
            start_row, start_col, end_row, end_col, pawn_color
        ) or self._check_is_valid_attack_move(
            start_row, start_col, end_row, end_col, pawn_color
        )

    def _check_is_valid_normal_move(
        self, start_row, start_col, end_row, end_col, pawn_color
    ):
        if start_col != end_col:
            return False

        if pawn_color == WHITE:
            expected_end_row = start_row + WHITE_DIRECTION
        else:
            expected_end_row = start_row + BLACK_DIRECTION
        if expected_end_row != end_row:
            return False

        if self.get_pawn(end_row, end_col) != EMPTY:
            return False

        return True

    def _check_is_valid_attack_move(
        self, start_row, start_col, end_row, end_col, pawn_color
    ):
        if abs(start_col - end_col) != 1:
            return False

        if pawn_color == WHITE:
            expected_end_row = start_row + WHITE_DIRECTION
        else:
            expected_end_row = start_row + BLACK_DIRECTION
        if expected_end_row != end_row:
            return False

        opposing_pawn_color = BLACK if pawn_color == WHITE else WHITE
        if self.get_pawn(end_row, end_col) != opposing_pawn_color:
            return False

        return True

    def __str__(self):
        result = ""
        for row in range(SIZE):
            result += (
                " | ".join([self.get_pawn(row, col) for col in range(SIZE)]) + "\n"
            )
        return result
