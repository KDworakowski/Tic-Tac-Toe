import pytest
from logic import Logic

def test_player_1_and_2_entering_the_game():
    player1 = Logic.Player(1)
    player2 = Logic.Player(2)

    dashboard = Logic.DashBoard()

    dashboard.add_player(player1)
    dashboard.add_player(player2)

    assert len(dashboard.players) == 2

def test_turn_randomize():
    players = [1,2]

    dashboard = Logic.DashBoard()

    dashboard.turn_randomize(players)
    print(players)
