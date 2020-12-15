from hexapawn import SIZE, WHITE, BLACK_DIRECTION, WHITE_DIRECTION
from random import choice


def get_random_move(board, color):
    print("Choosing random move...")
    print()
    valid_moves = []
    for row in range(SIZE):
        for col in range(SIZE):
            if board.get_pawn(row, col) == color:
                direction = WHITE_DIRECTION if color == WHITE else BLACK_DIRECTION
                if board.check_is_valid_move(row, col, row + direction, col):
                    valid_moves.append((row, col, row + direction, col))
                if board.check_is_valid_move(row, col, row + direction, col + 1):
                    valid_moves.append((row, col, row + direction, col + 1))
                if board.check_is_valid_move(row, col, row + direction, col - 1):
                    valid_moves.append((row, col, row + direction, col - 1))
    return choice(valid_moves)
