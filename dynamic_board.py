def board():
    board = []
    board_size = 5
    check_if_int = isinstance(board_size, int)
    if check_if_int != True:
        print("Board size must be an integer")
    elif board_size <= 2:
        print("Board size is minimum 3")
    elif board_size == 3 or board_size >= 3:
        for r in range(0, board_size):
            board.append([0 for c in range(0, board_size)])
        # print(board)
        return board

board()
# print(board)
