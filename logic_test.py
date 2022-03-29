import pytest
from logic import Logic


@pytest.mark.parametrize("test_input", [2, 3, 8])
def test_player_1_and_2_entering_the_game(test_input):
    dashboard = Logic.DashBoard()

    for a in range(test_input):
        dashboard.add_player(Logic.Player(a+1))

    assert len(dashboard.players) == test_input
    dashboard.players.clear()

def test_board_is_being_created():
    board = Logic.Board(3)

    assert isinstance(board.board, list)

@pytest.mark.parametrize("test_input, expected", [(3, True), (4, True), (0.4, False), ("5", False)])
def test_check_if_the_board_size_is_an_integer(test_input, expected):
    test = Logic.Board(test_input)
    assert bool(len(test.board)) == expected

@pytest.mark.parametrize("test_input, expected", [(3, True), (4, True), (0, False), (1, False)])
def test_check_if_the_board_size_is_not_smaller_than_3(test_input, expected):
    test = Logic.Board(test_input)
    assert bool(len(test.board)) == expected

def test_all_possible_winning_combinations():
    every_combination = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],

        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],

        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]]
    ]

    test_combination = Logic.Board.all_possible_winning_combinations()

    assert test_combination == every_combination


@pytest.mark.parametrize("test_input", [2, 3, 8])
def test_turn_randomize(test_input):

    dashboard = Logic.DashBoard()

    for a in range(test_input):
        dashboard.add_player(Logic.Player(a+1))

    dashboard.turn_randomize()
    assert dashboard.player_turn != 0

    dashboard.player_turn = test_input
    dashboard.choose_next_player()
    assert dashboard.player_turn == 1

    dashboard.choose_next_player()
    assert dashboard.player_turn == 2

    dashboard.players.clear()



def test_player_pawn_id():
    id = 1
    player = Logic.Player(id)

    pawn =  player.pawner.create()

    assert player.id == pawn.player_id

def test_game_create():
    Game = Logic.Game()
    assert Game.id == 1

    assert isinstance(Game.board.board, list)

def test_game():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1

    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    assert game.board.board[0][1].player_id == game.dashboard.player_turn

    game.dashboard.players.clear()

def test_game_move_game_finished():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1

    game.finished = True
    assert game.finished == True

    move = game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    assert game.board.board[0][1] == 0
    # error code: "GAME_FINISHED": 100
    assert move == 100

    game.dashboard.players.clear()

def test_game_move_player_turn_mismatch():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1

    move = game.move(player = game.dashboard.players[game.dashboard.player_turn-2], coordinate=[0,1])
    assert game.board.board[0][1] == 0
    # error code: "PLAYER_TURN_MISMATCH": 101
    assert move == 101

    game.dashboard.players.clear()

def test_game_move_place_on_board_already_taken():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1

    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    assert game.board.board[0][1].player_id == game.dashboard.player_turn

    game.dashboard.player_turn = 2

    move = game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    assert game.board.board[0][1].player_id != game.dashboard.player_turn
    # error code: "PLACE_ON_BOARD_ALREADY_TAKEN": 102
    assert move == 102


    game.dashboard.players.clear()

def test_game_dynamic_switch_player():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.turn_randomize()

    first_player_turn = game.dashboard.player_turn

    game.dashboard.choose_next_player()
    index = len(game.dashboard.players)
    assert game.dashboard.player_turn == (first_player_turn+index)%index+1

    game.dashboard.players.clear()

def test_game_static_switch_player():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1

    game.dashboard.choose_next_player()
    assert game.dashboard.player_turn == 2

    game.dashboard.choose_next_player()
    assert game.dashboard.player_turn == 1

    game.dashboard.players.clear()

def test_check_win():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,0])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,2])
    game.check_win_or_draw()

    assert game.finished == True

    assert game.dashboard.results() == 1
    game.dashboard.players.clear()


def test_check_game_not_finished():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,0])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    game.dashboard.player_turn = 2
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,2])
    game.check_win_or_draw()

    assert game.finished == False
    game.dashboard.players.clear()

def test_check_draw():
    game = Logic.Game()
    game.dashboard.add_player(Logic.Player(1))
    game.dashboard.add_player(Logic.Player(2))
    game.dashboard.player_turn = 1
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,0])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,2])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[1,2])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[2,1])

    game.dashboard.player_turn = 2
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[0,1])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[1,0])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[1,1])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[2,0])
    game.move(player = game.dashboard.players[game.dashboard.player_turn-1], coordinate=[2,2])


    game.check_win_or_draw()

    assert game.finished == True
    game.dashboard.players.clear()
