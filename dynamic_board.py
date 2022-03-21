
# all_possible_winning_combinations = [
#     [[0,0], [0,1], [0,2]],
#     [[1,0], [1,1], [1,2]],
#     [[2,0], [2,1], [2,2]],

#     [[0,0], [1,0], [2,0]],
#     [[0,1], [1,1], [2,1]],
#     [[0,2], [1,2], [2,2]],

#     [[0,0], [1,1], [2,2]],
#     [[0,2], [1,1], [2,0]]
# ]

def all_possible_winning_combinations(board_size: int = 3):
    """
    x - horizontal
    y - vertical
    """
    every_combination = []

    #for horizontal combinations
    for x in range(0,board_size):
        new_row = []
        for y in range(0,board_size):
            new_row.append([x,y])
        every_combination.append(new_row)

    #for vertical combinations
    for x in range(0,board_size):
        new_row = []
        for y in range(0,board_size):
            new_row.append([y,x])
        every_combination.append(new_row)

    #for diagonal combinations
    new_diagonal = []
    for x in range(0,board_size):
        for y in range(0,board_size):
            if x == y:
                new_diagonal.append([x,y])

    every_combination.append(new_diagonal)

    #for diagonal combinations
    new_diagonal = []
    for x in range(0,board_size):
        for y in range(0,board_size):
            if x == y:
                new_diagonal.append([x,board_size-y-1])
    every_combination.append(new_diagonal)
    return every_combination

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
        print(board)
        return board

all_possible_winning_combinations()
# winning()
# print(board)
