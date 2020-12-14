from hexapawn import HexapawnGame
from strategy import get_console_move, get_random_move

if __name__ == "__main__":
    game = HexapawnGame(
        get_black_move=get_random_move, get_white_move=get_console_move
    )
    game.run()
