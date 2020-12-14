from hexapawn.HexapawnConstants import WHITE, BLACK, PRETTY_NAME
from hexapawn.HexapawnBoard import HexapawnBoard
from hexapawn.HexapawnException import HexapawnException


class HexapawnGame:
    def __init__(self, get_black_move, get_white_move):
        self.board = HexapawnBoard()
        self.player_move_function = {BLACK: get_black_move, WHITE: get_white_move}
        self.current_player = WHITE
        self.other_player = BLACK

    def next_move(self):
        if not self.board.has_legal_move(self.current_player):
            return (
                self.other_player,
                False,
                f"There are no valid moves for {PRETTY_NAME[self.current_player]}. {PRETTY_NAME[self.other_player]} wins!",
            )

        try:
            get_move = self.player_move_function[self.current_player]
            move = get_move(self.board, self.current_player)
            self.board.move_pawn(*move)

            if self.board.has_reached_other_side(self.current_player):
                return (
                    self.current_player,
                    False,
                    f"{PRETTY_NAME[self.current_player]} reached the other side of the board. {PRETTY_NAME[self.current_player]} wins!",
                )
            self.current_player, self.other_player = (
                self.other_player,
                self.current_player,
            )
        except HexapawnException as e:
            return None, True, e.message

        return None, False, ""

    def run(self):
        gameover = False
        while not gameover:
            print(self.board)
            winner, error, message = self.next_move()
            gameover = winner is not None
            if gameover:
                print(self.board)
            if gameover or error:
                print(message)
                print()
