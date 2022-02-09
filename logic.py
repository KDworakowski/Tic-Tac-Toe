from typing import Optional
from random import randint

class Logic():
    class Game():
        """
        For the purpouse of this project we assume that
        player1 has ID:1, and player2 has ID:2.
        """
        id: int
        player1: Optional[str]
        player2: Optional[str]

        """
        Board is being created
        """
        board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        player_turn: int
        player_win: int
        finished = False

        def __init__(self, id: str, player1: str, player2: str) -> None:
            self.id = id
            self.player1 = player1
            self.player2 = player2
            self.player_turn = 0
            self.player_win = 0
            self.score_board = {self.player1: 0, self.player2: 0}
            self.board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]

    all_possible_winning_combinations = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],

        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],

        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]]
    ]

    def __init__(self) -> None:
        self.game = False

    """
    Player turn being randomized
    """
    def draw_player_turn(self) -> None:
        self.game.player_turn = randint(1,2)

    """
    Player is being created
    """
    def create(self, player1: str = "player1", player2: str = "player2") -> bool:
        self.game = self.Game(player1, player2)
        self.draw_player_turn()
        return True

    """
    Player is making move
    """
    def move(self, player_id, coordinate: list) -> int:
        """
        Check if game isn't finished
        """
        if self.game.finished:
            return self.error_codes["GAME_FINISHED"]

        """
        Check if the right player is making move
        """
        if self.game.player_turn != player_id:
            return self.error_codes["PLAYER_TURN_MISMATCH"]

        """
        Check if place on boards isn't already taken
        """
        if self.game.board[coordinate[0]][coordinate[1]] != 0:
            return self.error_codes["PLACE_ON_BOARD_ALREADY_TAKEN"]

        """
        Accept the chose of player
        """
        self.game.board[coordinate[0]][coordinate[1]] = player_id

        """
        Check if player won by comparing board with winning combinations
        """
        for x in self.all_possible_winning_combinations:
            if not self.game.finished:
                result = 0
                if (self.game.board[x[0][0]][x[0][1]] == \
                    self.game.board[x[1][0]][x[1][1]] == \
                    self.game.board[x[2][0]][x[2][1]]
                ):
                    result = (
                        self.game.board[x[0][0]][x[0][1]] + \
                        self.game.board[x[1][0]][x[1][1]] + \
                        self.game.board[x[2][0]][x[2][1]]
                    )

                    """
                    Player win
                    """
                    if result == 3:
                        self.game.player_win = 1
                        self.game.finished = True

                    elif result == 6:
                        self.game.player_win = 2
                        self.game.finished = True

        """
        Check if there's a draw by checking that whole board is filled with player moves
        """
        zeros = 0
        for x in range(0,2):
            for y in range(0,2):
                if self.game.board[x][y] == 0:
                    zeros += 1

        """
        Draw
        """
        if zeros == 0 and not self.game.finished:
            self.game.finished = True

        """
        Swap the players
        """
        if not self.game.finished:
            self.game.player_turn = ((self.game.player_turn + 2) % 2) + 1
            # self.game.player_turn = ((1 + 2) % 2) + 1 = 2 | ((2 + 2) % 2) + 1 = 1
        """
        End of the game
        """
        return 0
