from array import array
import random

class Logic():

    class PawnFactory():
        def __init__(self, player_id: int) -> None:
            self.player_id = player_id

        player_id: int

        def create(self):
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
        pawner = 0

    class DashBoard():
        players = []

        def add_player(self, player):
            self.players.append(player)

        """
        Players turns being randomized
        """
        def turn_randomize(self, players):
            self.player_turn = random.choice(players)

        """
        Next player is being chosen
        """
        def choose_next_player(self):
            if not self.game.finished:
                self.game.player_turn = ((self.game.player_turn + 2) % 2) + 1

        """
        Show results
        """
        def results():
            pass

    class Board():
        pass

    class Game():

        def board(self):
            """
            Board is being created
            """
            board = []

            """
            Set the board size
            """
            board_size = 5
            check_if_int = isinstance(board_size, int)

            """
            Check if the board size is an integer

            Check if the board size is not smaller than 3

            Check if the board size equals 3 or is bigger than 3
            """
            if check_if_int != True:
                print("Board size must be an integer")

            elif board_size <= 2:
                print("Board size is minimum 3")
            elif board_size == 3 or board_size >= 3:
                """
                Create board with selected size
                """
                for r in range(0, board_size):
                    board.append([0 for c in range(0, board_size)])
                # print(board)
                return board

        player_turn: int
        player_win: int
        finished = False

        def __init__(self, id: int, board: array) -> None:
            self.id = id
            self.board = board

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

        Player is creating a pawn

        Player is placing a pawn in the selected place on the board
        """
        self.game.board[coordinate[0]][coordinate[1]] = player_id

        """
        Check if player won by comparing board with winning combinations

        Logic is setting basic result as 0 and counting all fields in the list.

        For example, if player with ID:1 placed his moves in one of the winning combinations,
        the logic is counting all of his moves inside the winning combinations.
        If in one of the winning combinations player moves equals 3 (in that case, if the player
        would have ID:2 then it would need to equal 6) then this player won.
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

        After successful move made by a player without win or draw logic swap the player,
        so another player can make his move.
        """
        if not self.game.finished:
            self.game.player_turn = ((self.game.player_turn + 2) % 2) + 1
            # self.game.player_turn = ((1 + 2) % 2) + 1 = 2 | ((2 + 2) % 2) + 1 = 1
        """
        End of the game
        """
        return 0
