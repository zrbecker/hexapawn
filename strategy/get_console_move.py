from hexapawn import PRETTY_NAME


def get_console_move(board, color):
    try:
        print(f"Select {PRETTY_NAME[color]} pawn")
        start_row = int(input("Row: "))
        start_col = int(input("Col: "))
        print()

        print("Where do you want to move?")
        end_row = int(input("Row: "))
        end_col = int(input("Col: "))
        print()

        return start_row, start_col, end_row, end_col
    except ValueError:
        print("Please enter a valid integer")
        print()
        return get_console_move(board, color)
    except KeyboardInterrupt:
        exit(1)
