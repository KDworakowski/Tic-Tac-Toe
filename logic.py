from __future__ import annotations
from array import array
import random
import math
class Logic():

    class PawnFactory():
        def __init__(self, player_id: int) -> None:
            self.player_id = player_id

        player_id: int

        def create(self) -> Logic.Pawn:
            return Logic.Pawn(self.player_id)

    class Pawn():
        def __init__(self, player_id: int) -> None:
            self.player_id = player_id

        player_id: int
    class Player():
        """
        Pawn factory is being created
        """
        def __init__(self, id: int) -> None:
            self.id = id
            self.pawner = Logic.PawnFactory(self.id)

        id: int
        nickname: str
        pawner: Logic.PawnFactory = None


    class DashBoard():
        players = []

        player_turn = 0
        player_win = 0

        def add_player(self, player: Logic.Player) -> None:
            self.players.append(player)

        """
        Players turns being randomized
        """
        def turn_randomize(self):
            self.player_turn = random.choice(range(len(self.players)))+1

        """
        Next player is being chosen
        """
        def choose_next_player(self):
            index = len(self.players)
            self.player_turn = ((self.player_turn + index) % index) + 1

        """
        Show results
        """
        def results(self):
            return self.player_win

    class Board():
        def __init__(self, board_size: int = 3):
            """
            Board is being created.
            """
            self.board = []
            self.board_size = board_size
            check_if_int = isinstance(self.board_size, int)

            """
            Check if the board size is an integer

            Check if the board size is not smaller than 3

            Check if the board size equals 3 or is bigger than 3
            """
            if check_if_int != True:
                print("Board size must be an integer")
            elif self.board_size <= 2:
                print("Board size is minimum 3")
            elif self.board_size >= 3:
                for r in range(0, self.board_size):
                    self.board.append([0 for c in range(0, self.board_size)])

        @staticmethod
        def all_possible_winning_combinations(board_size: int = 3):
            """
            Create all possible winning combinations.

            x - horizontal
            y - vertical
            """

            """
            Create empty list for all winning combinations.
            """
            every_combination = []

            """
            Creating horizontal winning combinations and append them to list.
            """
            for x in range(0,board_size):
                new_row = []
                for y in range(0,board_size):
                    new_row.append([x,y])
                every_combination.append(new_row)

            """
            Creating horizontal winning combinations and append them to list.
            """
            for x in range(0,board_size):
                new_row = []
                for y in range(0,board_size):
                    new_row.append([y,x])
                every_combination.append(new_row)

            """
            Creating horizontal winning combinations and append them to list.
            """
            new_diagonal = []
            for x in range(0,board_size):
                for y in range(0,board_size):
                    if x == y:
                        new_diagonal.append([x,y])
            every_combination.append(new_diagonal)

            """
            Creating horizontal winning combinations and append them to list.
            """
            new_diagonal = []
            for x in range(0,board_size):
                for y in range(0,board_size):
                    if x == y:
                        new_diagonal.append([x,board_size-y-1])
            every_combination.append(new_diagonal)
            """
            Return every combination list.
            """
            return every_combination
    class Game():
        """
        Game create
        """
        player_turn: int
        player_win: int
        finished = False

        error_codes = {
        "GAME_FINISHED": 100,
        "PLAYER_TURN_MISMATCH": 101,
        "PLACE_ON_BOARD_ALREADY_TAKEN": 102,
        }

        def __init__(self, id: int = 1) -> None:
            self.id = id
            self.board = Logic.Board()
            self.dashboard = Logic.DashBoard()
            self.players = Logic.DashBoard.players
            self.player_turn = Logic.DashBoard.player_turn

        def move(self, player: Logic.Player, coordinate: list) -> int:
            """
            Check if game isn't finished
            """
            if self.finished:
                return self.error_codes["GAME_FINISHED"]

            """
            Check if the right player is making move
            """
            if self.dashboard.player_turn != player.id:
                return self.error_codes["PLAYER_TURN_MISMATCH"]

            """
            Check if place on boards isn't already taken
            """
            if isinstance(self.board.board[coordinate[0]][coordinate[1]], Logic.Pawn):
                return self.error_codes["PLACE_ON_BOARD_ALREADY_TAKEN"]

            """
            Accept the chose of player

            Player is creating a pawn

            Player is placing a pawn in the selected place on the board
            """

            self.board.board[coordinate[0]][coordinate[1]] = player.pawner.create()

            """
            Check if player won by comparing board with winning combinations

            Logic is setting basic result as 0 and counting all fields in the list.

            For example, if player with ID:1 placed his moves in one of the winning combinations,
            the logic is counting all of his moves inside the winning combinations.
            If in one of the winning combinations player moves equals 3 (in that case, if the player
            would have ID:2 then it would need to equal 6) then this player won.
            """
        def check_win_or_draw(self):
            for x in self.board.all_possible_winning_combinations():
                if not self.finished:
                    if ((isinstance(self.board.board[x[0][0]][x[0][1]], Logic.Pawn) and \
                        isinstance(self.board.board[x[1][0]][x[1][1]], Logic.Pawn) and \
                        isinstance(self.board.board[x[2][0]][x[2][1]], Logic.Pawn)) and \
                        (self.board.board[x[0][0]][x[0][1]].player_id == \
                        self.board.board[x[1][0]][x[1][1]].player_id == \
                        self.board.board[x[2][0]][x[2][1]].player_id)
                    ):

                        """
                        Player win
                        """
                        self.dashboard.player_win = self.board.board[x[0][0]][x[0][1]].player_id
                        self.finished = True

            """
            Check if there's a draw by checking that whole board is filled with pawns
            """
            pawn = 0
            for x in range(0,self.board.board_size):
                for y in range(0,self.board.board_size):
                    if isinstance(self.board.board[x][y], Logic.Pawn):
                        pawn += 1

            """
            Draw
            """
            if pawn == math.pow(self.board.board_size, 2) and not self.finished:
                self.finished = True

            """
            End of the game
            """
            return 0


#######################################
