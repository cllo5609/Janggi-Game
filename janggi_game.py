# Author: Clint Lohr
# Date: 02/19/2021
# Description: Creates a playable Janggi board game for two players. The players are "BLUE" and "RED" with BLUE player
# starting the game. The objective is to Checkmate the other player's "General" piece. A general is in
# check if it can be captured by an opposing player's game piece on the next turn. A checkmate occurs when the player
# in check cannot make a move to get their general out of check. If checkmate occurs on a player's general, the
# opposing player wins and the game is over.


class Pieces:

    """
    Represents a game piece object. This class is responsible for initializing the game piece object with a player, a
    starting row, starting column, and an empty list to store current moves in. This class will serve as a parent
    function for each piece's class.
    """

    def __init__(self, player, column, row):

        """
        Initializes the Pieces class with a player, column, row, and current moves list.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        self._player = player
        self._row = row
        self._column = column
        self._current_moves = []

    def get_column(self):

        """
        Gets the column that the piece object is positioned at on the game board.
        :return: The column as an integer.
        """
        return self._column

    def set_column(self, column):

        """
        Sets the column that piece object will be positioned at on the game board.
        :param column: Represents the column that the piece object is positioned at on the board as an integer.
        :return: NONE
        """

        self._column = column

    def get_row(self):

        """
        Gets the row that the piece object is positioned at on the game board.
        :return: The row as an integer.
        """

        return self._row

    def set_row(self, row):

        """
        Sets the row that piece object will be positioned at on the game board.
        :param row: Represents the column that the piece object is positioned at on the board as an integer.
        :return: NONE
        """

        self._row = row

    def get_player(self):

        """
        Gets the player that the piece object belongs to.
        :return: The player as a string.
        """

        return self._player

    def get_current_moves(self):

        """
        Gets the current moves that the piece object can make on the board.
        :return: A list of lists containing move positions.
        """

        return self._current_moves

    def set_current_moves(self, moves_list):

        """
        Removes the current moves from the move list and appends the new move list to the current move list for that
        piece object.
        :param moves_list: Represents a list containing lists of moves that the piece object can make on the board.
        :return: NONE
        """

        self._current_moves = []
        for move in moves_list:
            self._current_moves.append(move)


class General(Pieces):

    """
    Represents a General type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the General game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the General game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "General"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a General game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a General game piece object.
        :return: Returns the piece objects name as a sting.
        """

        return self._name

    def create_name(self, player):

        """
        Creates the name for the General piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """

        if player == "BLUE":
            return "bGn"
        else:
            return "rGn"


class Guard(Pieces):

    """
    Represents a Guard type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the Guard game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the Guard game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "Guard"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a Guard game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a Guard game piece object.
        :return: Returns the piece objects name as a sting.
        """

        return self._name

    def create_name(self, player):

        """
        Creates the name for the Guard piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """

        if player == "BLUE":
            return "bGd"
        else:
            return "rGd"


class Horses(Pieces):

    """
    Represents a Horse type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the Horse game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the General game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "Horse"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a Horse game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a Horse game piece object.
        :return: Returns the piece objects name as a sting.
        """
        return self._name

    def create_name(self, player):

        """
        Creates the name for the Horse piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """

        if player == "BLUE":
            return "bHs"
        else:
            return "rHs"


class Elephants(Pieces):

    """
    Represents a Elephant type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the Elephant game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the Elephant game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "Elephant"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a Elephant game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a Elephant game piece object.
        :return: Returns the piece objects name as a sting.
        """

        return self._name

    def create_name(self, player):

        """
        Creates the name for the Elephant piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """

        if player == "BLUE":
            return "bEl"
        else:
            return "rEl"


class Chariots(Pieces):

    """
    Represents a Chariot type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the Chariot game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the Chariot game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "Chariot"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a Chariot game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a Chariot game piece object.
        :return: Returns the piece objects name as a sting.
        """

        return self._name

    def create_name(self, player):

        """
        Creates the name for the Chariot piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """


        if player == "BLUE":
            return "bCh"
        else:
            return "rCh"


class Cannons(Pieces):

    """
    Represents a Cannon type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the Cannon game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the Cannon game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "Cannon"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a Cannon game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a Cannon game piece object.
        :return: Returns the piece objects name as a sting.
        """
        return self._name

    def create_name(self, player):

        """
        Creates the name for the Cannon piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """

        if player == "BLUE":
            return "bCn"
        else:
            return "rCn"


class Soldiers(Pieces):

    """
    Represents a Soldier type piece object. Inherits from the Pieces class. This sub class is responsible for
    initializing the Soldier game piece object with a piece type and piece name. Contains methods for getting data
    members and creating the piece object name.
    """

    def __init__(self, player, column, row):

        """
        Initializes the Soldier game piece. Inherits from the Pieces class. Initializes the piece object type and
        name. Name is abbreviated as with the player in which the belongs to and the piece name.
        :param player: Represents a player that the game piece belongs to as a string.
        :param column: Represents the column on the board that the game piece is position at as an integer.
        :param row: Represents the row on the board that the game piece is position at as an integer.
        """

        super().__init__(player, column, row)
        self._type = "Soldier"
        self._name = self.create_name(player)

    def get_type(self):

        """
        Gets the piece type for a Soldier game piece object.
        :return: Returns the piece type as a sting.
        """

        return self._type

    def get_name(self):

        """
        Gets the name for a Soldier game piece object.
        :return: Returns the piece objects name as a sting.
        """

        return self._name

    def create_name(self, player):

        """
        Creates the name for the Soldier piece object as a string. The name is an abbreviation of the player and the
        piece type as a sting.
        :param player: Represents the player that the piece object belongs to as a string.
        :return: Returns the piece object's name as a sting.
        """

        if player == "BLUE":
            return "bSd"
        else:
            return "rSd"


class JanggiGame:

    """
    Represents the Janggi game in which the game is played. This class is responsible for creating the board, game
    pieces, and game states and placing pieces in their starting locations. This class is also responsible for
    defining, validating and carrying out moves made throughout the game. This class contains a method that
    communicates with the pieces class in order to define each game piece.
    """

    def __init__(self):
        """
        Initializes the data members for the JanggiGame class. This includes initializing the board, pieces, game state
        player turn, check, check count, and checkmate. The self._pieces data member calls a method which communicates
        with the Pieces Class to define each piece. This method takes no parameters and does not return anything.
        """

        self._board = self.create_board()
        self._pieces = self.create_pieces()
        self._game_state = "UNFINISHED"
        self._player_turn = "BLUE"
        self._check = False
        self._checkmate = False
        self._checked_coor = []


    def get_board(self):

        """
        Gets the current board
        :return: The current board
        """

        return self._board


    def set_board(self, piece, row, column):

        """
        Sets each game piece on the board at a given list index represented as rows and columns.
        :param piece: Represents a game piece object.
        :param row: Represents a row on the board.
        :param column: Represents a column on the board.
        :return: NONE
        """

        self._board[row][column] = piece


    def get_pieces(self):

        """
        Gets a list of the current pieces.
        :return: A list of the current pieces
        """

        return self._pieces


    def get_game_state(self):

        """
        Gets the current game state, either "RED_WON", "BLUE_WON", or "UNFINISHED".
        :return: A string with the current game state.
        """

        return self._game_state


    def set_game_state(self, status):

        """
        Sets the current game status.
        :param status: Represents the current game state, either "RED_WON", "BLUE_WON", or "UNFINISHED".
        :return: NONE
        """

        self._game_state = status


    def get_player_turn(self):

        """
        Gets the current player's turn, either "BLUE" OR "RED".
        :return: The current player's turn as a string.
        """

        return self._player_turn


    def set_player_turn(self, player):

        """
        Sets the player's turn for the next round.
        :param player: Represents the current player as a string.
        :return: NONE
        """

        if player == "RED":
            self._player_turn = "BLUE"

        if player == "BLUE":
            self._player_turn = "RED"


    def get_check(self):

        """
        Gets the status of check.
        :return: The status of check, either False or the player in check as a string.
        """

        return self._check


    def set_check(self, player):

        """
        Sets check to the player in check.
        :param player: Represents the player to be placed in check as a string.
        :return: NONE
        """

        self._check = player


    def get_checkmate(self):

        """
        Gets the status of checkmate.
        :return: The status of checkmate, either True or False.
        """

        return self._checkmate


    def set_checkmate(self, player):

        """
        Sets the checkmate status to either True or False and sets the game state to show the winning player.
        :param player: Represents the losing player as a string.
        :return: NONE
        """

        if player == "RED":
            self._checkmate = True
            self.set_game_state("BLUE_WON")

        if player == "BLUE":
            self._checkmate = True
            self.set_game_state("RED_WON")


    def is_in_check(self, player):

        """
        Takes a a parameter the name of a player as a string. Calls self.get_check and return True if self._check
        is equal to that player and False otherwise.
        :param player: Represents the player to check the check status for as a string.
        :return: Returns True if the player is in check and False otherwise.
        """

        player = player.upper()
        if player == self.get_check():
            return True

        return False

    def get_checked_coor(self):

        """
        Gets the coordinates of the General in check.
        :return: Returns the coordinates of the General in check.
        """

        return self._checked_coor

    def set_checked_coor(self, coord):

        """
        Sets the coordinates of the General in check.
        :param coord: Represents the coordinates of the game piece as a list.
        :return: NONE
        """

        self._checked_coor = coord


    def create_board(self):
        """
        Creates the board in which the game will be played on by creating a list of lists with specified rows and
        columns.
        :return: The board that the game will played on as a list of lists.
        """

        board = [["   "] * 9 for row in range(10)]
        return board


    def create_pieces(self):

        """
        Defines the pieces that will be used in the game. The pieces are stored in a list. Each piece calls its specific
        class to define and initialize the piece with a player, starting row, and starting column. Calls the place
        pieces method after the pieces are defined.
        :return: A list of all starting game pieces.
        """

        pieces = [
            Chariots("RED", 0, 0), Elephants("RED", 1, 0), Horses("RED", 2, 0), Guard("RED", 3, 0), Guard("RED", 5, 0),
            Elephants("RED", 6, 0), Horses("RED", 7, 0), Chariots("RED", 8, 0), General("RED", 4, 1),
            Cannons("RED", 1, 2), Cannons("RED", 7, 2), Soldiers("RED", 0, 3), Soldiers("RED", 2, 3),
            Soldiers("RED", 4, 3), Soldiers("RED", 6, 3), Soldiers("RED", 8, 3), Soldiers("BLUE", 0, 6),
            Soldiers("BLUE", 2, 6), Soldiers("BLUE", 4, 6), Soldiers("BLUE", 6, 6), Soldiers("BLUE", 8, 6),
            Cannons("BLUE", 1, 7), Cannons("BLUE", 7, 7), General("BLUE", 4, 8), Chariots("BLUE", 0, 9),
            Elephants("BLUE", 1, 9), Horses("BLUE", 2, 9), Guard("BLUE", 3, 9), Guard("BLUE", 5, 9),
            Elephants("BLUE", 6, 9), Horses("BLUE", 7, 9), Chariots("BLUE", 8, 9)
        ]

        # Called to place pieces after they are defined.
        self.place_piece(pieces)
        return pieces


    def place_piece(self, pieces):

        """
        Places each game piece on the board with a specified row and column.
        :param pieces: Represents a list of all game pieces.
        :return: NONE
        """

        for piece in pieces:
            row = Pieces.get_row(piece)
            column = Pieces.get_column(piece)
            self._board[row][column] = piece


    def coordinates_conversion_dict(self, column, row):

        """
        Uses a dictionary to convert the current position and move to position from algebraic notion to list index positions for the
        rows and columns.
        :param column: Represents a column on the board for the current and move to positions.
        :param row: Represents a row on the board for the current and move to positions.
        :return: Returns the converted row and column positions as a list.
        """

        conversion_dict_1 = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8
        }

        conversion_dict_2 = {
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6,
            "8": 7,
            "9": 8,
            "10": 9
        }

        column = conversion_dict_1[column]
        row = conversion_dict_2[row]
        return [row, column]


    def make_move(self, cur_pos, move_pos):

        """
        Takes parameters for the current piece's position on the board and the coordinates of the piece's destination.
        Moves current player's piece to its new position on the board. It is responsible for checking the game
        status and returning True if the move was successful. This method calls other functions in order to check the
        validity of the coordinates, convert current and move to coordinates, check if the player is skipping a turn,
        and initiate the move.
        :param cur_pos: Represents the current position of a piece on the board in algebraic notation as a string.
        :param move_pos: Represents the move to position of a piece on the board in algebraic notation as a string.
        :return: True if the move was successful and False otherwise.
        """

        # Checks if a player has won the game or if the game is still in play.
        if self.get_game_state() != "UNFINISHED":
            return False

        # Creates lists of the the current and move to coordinates. Converts '1', '0' to '10'.
        board = self.get_board()
        current = list(cur_pos)
        if '1' and '0' in current:
            current = [current[0], '10']

        move_to = list(move_pos)
        if '1' and '0' in move_to:
            move_to = [move_to[0], '10']

        # Calls a method to check if the current and move to coordinates are valid. Returns False if invalid.
        coordinates_check = self.coordinates_check(current, move_to)
        if not coordinates_check:
            return False

        # Calls a method to convert the current and move to coordinates into list indexes and assigns them to a
        # variable.
        current = self.coordinates_conversion_dict(current[0], current[1])
        move_to = self.coordinates_conversion_dict(move_to[0], move_to[1])
        piece_obj = board[current[0]][current[1]]

        # Conditional statement that runs if the current and move to positions are the same. Calls a method to check
        # if a player is allowed to skip their turn and returns False if they cannot skip.
        if current == move_to:
            skip_turn_check = self.skip_turn_check(piece_obj, current)
            if not skip_turn_check:
                return False
            return True

        # Calls a method for the current and move to position to check if the move is valid. Returns False
        # if it is not a valid move.
        cur_check = self.cur_pos_check(piece_obj, current)
        move_check = self.move_pos_check(move_to)
        if not cur_check and move_check:
            return False

        # Calls a method to initiate the move. Returns False if the move cannot be made.
        move_setup = self.move_check(piece_obj, current, move_to)
        if not move_setup:
            return False

        # Switches the player's turn if the move was successful and returns True.
        self.set_player_turn(self.get_player_turn())
        player = self.get_player_turn()

        # Checks if checked general is checkmated
        if self.get_check() == player:
            if self.check_checkmate():
                self.set_checkmate(self._player_turn)
            self.set_check(player)
        return True


    def coordinates_check(self, cur_pos, move_pos):

        """
        Called by the make_moves method to check if the current and move to positions are within the range of the board.
        :param cur_pos: Represents the current position of a game piece in algebraic notation as a string.
        :param move_pos: Represents the current position of a game piece in algebraic notation as a string.
        :return: True if the coordinates are valid and False otherwise.
        """

        # Checks that the columns are in range on the board.
        valid_coord = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        if cur_pos[0] not in valid_coord:
            return False

        # Checks if the rows are in range on the board.
        if int(cur_pos[1]) not in range(1, 11):
            return False

        if move_pos[0] not in valid_coord:
            return False

        if int(move_pos[1]) not in range(1, 11):
            return False

        return True


    def cur_pos_check(self, piece_obj, cur_pos):

        """
        Called by the make_move method to check that the game piece at the current position exists and that it is the
        correct player's piece.
        :param piece_obj: Represents a game piece object on the board.
        :param cur_pos: Represents the current position of the game piece as a list.
        :return: True if the game piece exists and belongs to the current player and False otherwise.
        """

        board = self.get_board()
        if board[cur_pos[0]][cur_pos[1]] == "   ":
            return False

        player = piece_obj.get_player()
        if player != self.get_player_turn():
            return False

        return True


    def move_pos_check(self, move_pos):

        """
        Called by the make move method to check whether the desired move to position contains a game piece that belongs
        to the current player. Returns False if this is the case.
        :param move_pos: Represents the move to position for a game piece as a list.
        :return: True if the move to position is valid and False otherwise.
        """

        board = self.get_board()
        position = board[move_pos[0]][move_pos[1]]

        if position == "   ":
            return True

        player = position.get_player()
        if player == self.get_player_turn():
            return False

        return True


    def skip_turn_check(self, piece_obj, cur_pos):

        """
        Called if the current and move to positions match. This tells the game that the current player wishes to skip
        their turn. Checks if the current player is in check, if true the player cannot skip their turn and it returns
        False. If the player is able to skip their turn, the player turn is changed to the next player.
        :param piece_obj: Represents a game piece object.
        :param cur_pos: Represents the coordinates of the current position as a list.
        :return: True if the player is able to skip their turn or False otherwise
        """

        # Checks if their is a game piece at that position.
        board = self.get_board()
        if board[cur_pos[0]][cur_pos[1]] == "   ":
            return False

        # Checks if the current player is in check.
        player = piece_obj.get_player()
        if self.is_in_check(player):
            return False

        # Changes the players turn to the appropriate player if the current player can skip their turn.
        if self.get_player_turn() == "RED":
            self.set_player_turn("RED")
            return True

        if self.get_player_turn() == "BLUE":
            self.set_player_turn("BLUE")
            return True


    def current_moves(self, piece_obj):

        """
        Called by the move_check method which takes a piece object and calls the appropriate moves method for that
        piece object. The moves method will find all possible moves for that piece given its current position and
        return a list of those moves as a list. Those moves are then set to that pieces moves list defined in the
        Pieces class.
        :param piece_obj: Represents a game piece object.
        :return: Returns the valid moves for a game piece object as a list.
        """

        piece_type = piece_obj.get_type()
        player = piece_obj.get_player()

        if piece_type == "General":
            moves = self.general_and_guard_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        elif piece_type == "Guard":
            moves = self.general_and_guard_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        elif piece_type == "Horse":
            moves = self.horse_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        elif piece_type == "Elephant":
            moves = self.elephant_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        elif piece_type == "Chariot":
            moves = self.chariot_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        elif piece_type == "Cannon":
            moves = self.cannon_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        elif piece_type == "Soldier":
            moves = self.soldier_moves(piece_obj, player)
            piece_obj.set_current_moves(moves)

        return moves


    def move_check(self, piece_obj, cur_pos, move_to):

        """
        Calls the current_moves method for the game piece object at the current position and checks if the desired
        move to position is in that list. If True then the move is valid or False otherwise. Checks if the current
        player is in check and calls the check_check method if True. If the player is not currently in check, the
        current_moves method is called for each game piece still in play and updates its current moves.
        :param piece_obj: Represents a game piece object.
        :param cur_pos: Represents the current position of a game piece as a list.
        :param move_to: Represents the move to position of a game piece as a list.
        :return: True if the move is valid and the player is not in check or False otherwise.
        """

        # Checks if the desired move is in the current piece object's move list.
        current_piece_moves = self.current_moves(piece_obj)
        if move_to not in current_piece_moves:
            return False

        # Checks if the player is in check and calls the check_check method if True.
        if self._check == self.get_player_turn():
            return False


        # Initiates the player's desired move and updates the move list for each piece on the board.
        self.initiate_move(piece_obj, cur_pos, move_to)
        for piece in self.get_pieces():
            self.current_moves(piece)

        return True

    def check_checkmate(self):

        """
        Called by the make_move method to check for a checkmate. Moves the piece to
        the move to position, removes the game piece object from the pieces list if an opponent's piece was captured,
        sets the previous position to "   " and sets the new row and column for the game piece object by calling
        set methods in the Pieces class.
        :param piece_obj: Represents a game piece object.
        :param cur_pos: Represents the current position of a game piece as a list.
        :param move_to: Represents the move to position of a game piece as a list.
        :return: True if a player is Checkmated, False if the player is only in Check
        """

        gen_coor = self.get_checked_coor()
        gen_obj = self._board[gen_coor[0]][gen_coor[1]]
        gen_moves = self.current_moves(gen_obj)

        for move in gen_moves:
            flag = False
            self._check = False
            self.initiate_move(gen_obj, gen_coor, move)
            for piece in self.get_pieces():
                self.current_moves(piece)

            if self._check:
                flag = True

            self.initiate_move(gen_obj, move, gen_coor)
            for piece in self.get_pieces():
                self.current_moves(piece)

            if not flag:
                return False

        return True


    def initiate_move(self, piece_obj, cur_pos, move_to):

        """
        Called by the move_check and check_check methods to initiate the current player's move. Moves the piece to
        the move to position, removes the game piece object from the pieces list if an opponent's piece was captured,
        sets the previous position to "" and sets the new row and column for the game piece object by calling
        set methods in the Pieces class.
        :param piece_obj: Represents a game piece object.
        :param cur_pos: Represents the current position of a game piece as a list.
        :param move_to: Represents the move to position of a game piece as a list.
        :return: NONE
        """

        move_to_piece = self._board[move_to[0]][move_to[1]]
        if move_to_piece != "   ":
            self._pieces.remove(move_to_piece)
        self.set_board("   ", cur_pos[0], cur_pos[1])
        self.set_board(piece_obj, move_to[0], move_to[1])
        piece_obj.set_row(move_to[0])
        piece_obj.set_column(move_to[1])


    def general_check(self, move):

        """
        Called by each of the piece's moves method to check if one of the moves in their moves list will put an
        opposing player's General in check. If True, 1 is added to the check count and self._check is set to the
        player in check.
        :param move: Represents a list of all valid moves for a game piece.
        :return: NONE
        """

        board = self.get_board()
        row = move[0]
        column = move[1]

        # Called if a move can capture an opposing player's game piece.
        if board[row][column] != "   ":
            piece = board[row][column]
            piece_type = piece.get_type()
            player = piece.get_player()

            # Called if the game piece that can be captured is a General.
            if piece_type == "General":
                self.set_check(player)
                self.set_checked_coor([row, column])


    def general_and_guard_moves(self, piece_obj, player):

        """
        Called by the current_moves method. Defines all possible movements that the General and Guard can make.
        Calls the general_and_guard_moves_list for each of the game piece's possible movements. Uses the list created by
        the general_and_guard_moves_list method and calls the general_checks method to see if any of the moves in the
        list will put an opposing player's General in check.
        :param piece_obj: Represents a game piece object.
        :param player: Represents the player for the game piece object.
        :return: A list of all valid moves for a game piece object.
        """
        row = piece_obj.get_row()
        column = piece_obj.get_column()
        moves = []

        # All possible move patterns for the General and Guard.
        self.general_and_guard_moves_list(player, row, column, 0, 1, moves)
        self.general_and_guard_moves_list(player, row, column, 0, -1, moves)
        self.general_and_guard_moves_list(player, row, column, 1, 0, moves)
        self.general_and_guard_moves_list(player, row, column, -1, 0, moves)

        if (column == 4 and (row == 1 or row == 8)) or (column != 4 and (row != 1 and row != 8)):
            self.general_and_guard_moves_list(player, row, column, 1, 1, moves)
            self.general_and_guard_moves_list(player, row, column, -1, -1, moves)
            self.general_and_guard_moves_list(player, row, column, 1, -1, moves)
            self.general_and_guard_moves_list(player, row, column, -1, 1, moves)

        for move in moves:
            self.general_check(move)
        return moves


    def general_and_guard_moves_list(self, player, row, column, r, c, moves):

        """
        Called by the general_and_guard_moves method. This method defines what moves can be made for these game
        pieces. It checks whether a move is valid based on these definitions and where friendly and opposing pieces
        are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """

        # Move parameters for a General or Guard in the red palace.
        board = self.get_board()
        if player == "RED":
            # Checks that the move is in range of the board and palace.
            if row + r in range(3) and column + c in range(3, 6):
                if board[row + r][column + c] != "   ":
                    occupant = board[row + r][column + c]
                    occ_player = occupant.get_player()
                    if occ_player == player:
                        return moves
                    moves.append([row + r, column + c])
                moves.append([row + r, column + c])

        # Move parameters for a General or Guard in the blue palace.
        if player == "BLUE":
            if row + r in range(7, 10) and column + c in range(3, 6):
                if board[row + r][column + c] != "   ":
                    occupant = board[row + r][column + c]
                    occ_player = occupant.get_player()
                    if occ_player == player:
                        return moves
                    moves.append([row + r, column + c])
                moves.append([row + r, column + c])

        return moves


    def horse_moves(self, piece_obj, player):

        """
        Called by the current_moves method. Defines all possible movements that the Horse piece can make.
        Calls the horse_moves_list for each of the game piece's possible movements. Uses the list created by
        the horse_moves_list method and calls the general_checks method to see if any of the moves in the
        list will put an opposing player's General in check.
        :param piece_obj: Represents a game piece object.
        :param player: Represents the player for the game piece object.
        :return: A list of all valid moves for a game piece object.
        """

        row = piece_obj.get_row()
        column = piece_obj.get_column()
        moves = []

        self.horse_moves_list(player, row, column, 0, 1, 1, 1, moves)
        self.horse_moves_list(player, row, column, 0, -1, -1, -1, moves)
        self.horse_moves_list(player, row, column, 0, 1, -1, 1, moves)
        self.horse_moves_list(player, row, column, 0, -1, 1, -1, moves)

        self.horse_moves_list(player, row, column, 1, 0, 1, 1, moves)
        self.horse_moves_list(player, row, column, 1, 0, 1, -1, moves)
        self.horse_moves_list(player, row, column, -1, 0, -1, -1, moves)
        self.horse_moves_list(player, row, column, -1, 0, -1, 1, moves)

        for move in moves:
            self.general_check(move)
        return moves


    def horse_moves_list(self, player, row, column, r, c, dr, dc, moves):

        """
        Called by the horse_moves method. This method defines what moves can be made for these game
        pieces. It checks whether a move is valid based on these definitions and where friendly and opposing pieces
        are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param dr: Represents the movement along a row for a diagonal move as an integer.
        :param dc: Represents the movement along a column for a diagonal move as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """

        board = self.get_board()
        # Checks if the move is in range of the board and that no piece is blocking the movement horizontally or
        # vertically.
        if row + r in range(10) and column + c in range(9):
            first_row = row + r
            first_col = column + c
            if board[first_row][first_col] != "   ":
                return moves

            # Checks if the move is in range of the board and that the move is valid for the diagonal movement.
            if first_row + dr in range(10) and first_col + dc in range(9):
                second_row = first_row + dr
                second_col = first_col + dc
                if board[second_row][second_col] != "   ":
                    occupant = board[second_row][second_col]
                    occ_player = occupant.get_player()
                    if occ_player == player:
                        return moves
                    moves.append([second_row, second_col])
                moves.append([second_row, second_col])
        return moves


    def elephant_moves(self, piece_obj, player):

        """
        Called by the current_moves method. Defines all possible movements that the Elephant piece can make.
        Calls the elephant_moves_list for each of the game piece's possible movements. Uses the list created by
        the elephant_moves_list method and calls the general_checks method to see if any of the moves in the
        list will put an opposing player's General in check.
        :param piece_obj: Represents a game piece object.
        :param player: Represents the player for the game piece object.
        :return: A list of all valid moves for a game piece object.
        """

        row = piece_obj.get_row()
        column = piece_obj.get_column()
        moves = []

        self.elephant_moves_list(player, row, column, 0, 1, 1, 1, moves)
        self.elephant_moves_list(player, row, column, 0, -1, 1, -1, moves)
        self.elephant_moves_list(player, row, column, 1, 0, 1, 1, moves)
        self.elephant_moves_list(player, row, column, 1, 0, 1, -1, moves)

        self.elephant_moves_list(player, row, column, 0, 1, -1, 1, moves)
        self.elephant_moves_list(player, row, column, 0, -1, -1, -1, moves)
        self.elephant_moves_list(player, row, column, -1, 0, -1, -1, moves)
        self.elephant_moves_list(player, row, column, -1, 0, -1, 1, moves)

        for move in moves:
            self.general_check(move)
        return moves

    def elephant_moves_list(self, player, row, column, r, c, dr, dc, moves):

        """
        Called by the elephant_moves method. This method defines what moves can be made for these game
        pieces. It checks whether a move is valid based on these definitions and where friendly and opposing pieces
        are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param dr: Represents the movement along a row for a diagonal move as an integer.
        :param dc: Represents the movement along a column for a diagonal move as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """
        # Checks if the move is in range of the board and that no piece is blocking the movement horizontally or
        # vertically.
        board = self.get_board()
        if row + r in range(10) and column + c in range(9):
            first_row = row + r
            first_col = column + c
            if board[first_row][first_col] != "   ":
                return moves

            # Checks if the move is in range of the board and that no piece is blocking the movement diagonally.
            if first_row + dr in range(10) and first_col + dc in range(9):
                second_row = first_row + dr
                second_col = first_col + dc
                if board[second_row][second_col] != "   ":
                    return moves

                # Checks if the move is in range of the board and that the move is valid for the second diagonal
                # movement.
                if second_row + dr in range(10) and second_col + dc in range(9):
                    third_row = second_row + dr
                    third_col = second_col + dc
                    if board[third_row][third_col] != "   ":
                        occupant = board[third_row][third_col]
                        occ_player = occupant.get_player()
                        if occ_player == player:
                            return moves
                        moves.append([third_row, third_col])
                    moves.append([third_row, third_col])
        return moves

    def chariot_moves(self, piece_obj, player):

        """
        Called by the current_moves method. Defines all possible movements that the Chariot piece can make.
        Calls the chariot_moves_list for each of the game piece's possible movements. Uses the list created by
        the chariot_moves_list method and calls the general_checks method to see if any of the moves in the
        list will put an opposing player's General in check.
        :param piece_obj: Represents a game piece object.
        :param player: Represents the player for the game piece object.
        :return: A list of all valid moves for a game piece object.
        """

        row = piece_obj.get_row()
        column = piece_obj.get_column()
        moves = []

        self.chariot_moves_list(player, row, column, 0, 1, moves)
        self.chariot_moves_list(player, row, column, 0, -1, moves)
        self.chariot_moves_list(player, row, column, 1, 0, moves)
        self.chariot_moves_list(player, row, column, -1, 0, moves)

        # Adds additional diagonal movement for the piece if the chariot is in a palace.
        if row in range(3) or range(7, 10):
            if column in range(3, 6):
                self.chariot_palace_moves(player, row, column, 1, 1, moves)
                self.chariot_palace_moves(player, row, column, -1, -1, moves)
                self.chariot_palace_moves(player, row, column, 1, -1, moves)
                self.chariot_palace_moves(player, row, column, -1, 1, moves)

        for move in moves:
            self.general_check(move)

        return moves

    def chariot_moves_list(self, player, row, column, r, c, moves):

        """
        Called by the chariot_moves method. This method defines what moves can be made for these game
        pieces. It checks whether a move is valid based on these definitions and where friendly and opposing pieces
        are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """

        # Checks that the move is in range of the board and if it is valid.
        if row + r in range(10) and column + c in range(9):
            next_row = row + r
            next_col = column + c
            if self._board[next_row][next_col] != "   ":
                occupant = self._board[next_row][next_col]
                occ_player = occupant.get_player()
                if occ_player != player:
                    moves.append([next_row, next_col])
                    return
                return
            else:
                moves.append([next_row, next_col])
                self.chariot_moves_list(player, next_row, next_col, r, c, moves)

    def chariot_palace_moves(self, player, row, column, r, c, moves):

        """
        Called by the chariot_moves method. This method defines what moves can be made for these game
        pieces if they are within a palace. It checks whether a move is valid based on these definitions and where
        friendly and opposing pieces are positioned on the current board. If a move is valid it is appended to the
        moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """

        # Checks that the move is in range of the board and if it is valid.
        if row + r in range(3) or range(7, 10):
            if column + c in range(3, 6):
                next_row = row + r
                next_col = column + c
                if self._board[next_row][next_col] != "   ":
                    occupant = self._board[next_row][next_col]
                    occ_player = occupant.get_player()
                    if occ_player != player:
                        moves.append([next_row, next_col])
                        return
                    return
                else:
                    moves.append([next_row, next_col])
                    self.chariot_palace_moves(player, next_row, next_col, r, c, moves)
        return moves

    def cannon_moves(self, piece_obj, player):

        """
        Called by the current_moves method. Defines all possible movements that the Cannon piece can make.
        Calls the cannon_moves_list for each of the game piece's possible movements. Uses the list created by
        the cannon_moves_list method and calls the general_checks method to see if any of the moves in the
        list will put an opposing player's General in check.
        :param piece_obj: Represents a game piece object.
        :param player: Represents the player for the game piece object.
        :return: A list of all valid moves for a game piece object.
        """

        row = piece_obj.get_row()
        column = piece_obj.get_column()
        moves = []
        jump_count = 0

        self.cannon_moves_list(player, row, column, 1, 0, moves, jump_count)
        self.cannon_moves_list(player, row, column, -1, 0, moves, jump_count)
        self.cannon_moves_list(player, row, column, 0, 1, moves, jump_count)
        self.cannon_moves_list(player, row, column, 0, -1, moves, jump_count)

        # Adds additional diagonal movement for the piece if it is in a palace.
        if row in range(0, 3) or row in range(7, 10):
            if column in range(3, 6):
                self.cannon_palace_list(player, row, column, 1, 1, moves, jump_count)
                self.cannon_palace_list(player, row, column, -1, -1, moves, jump_count)
                self.cannon_palace_list(player, row, column, 1, -1, moves, jump_count)
                self.cannon_palace_list(player, row, column, -1, 1, moves, jump_count)

        # Removes duplicates from the move list.
        no_duplicates = []
        for move in moves:
            if move not in no_duplicates:
                no_duplicates.append(move)

        for move in no_duplicates:
            self.general_check(move)

        return no_duplicates


    def cannon_moves_list(self, player, row, column, r, c, moves, jump_count):

        """
        Called by the cannon_moves method. This method defines what moves can be made for these game
        pieces. It checks whether a move is valid based on these definitions and where friendly and opposing pieces
        are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :param jump_count: Represents a counter to keep track of whether or not the cannon piece has jumped a piece.
        :return: A list containing lists of valid moves.
        """

        # Checks that the move is in range of the board and if it is valid.
        if row + r in range(10) and column + c in range(9):
            next_row = row + r
            next_col = column + c

            # Runs if the Cannon has already jumped a game piece.
            if jump_count == 1:
                if self._board[next_row][next_col] != "   ":
                    occupant = self._board[next_row][next_col]
                    piece_type = occupant.get_type()
                    occ_player = occupant.get_player()
                    # Checks if the game piece it encounters is a Cannon or a friendly.
                    if piece_type == "Cannon" or occ_player == player:
                        if self._board[row][column] != "   ":
                            return
                        moves.append([row, column])
                        return
                    moves.append([next_row, next_col])
                    return
                moves.append([next_row, next_col])

            # Runs if the Cannon has not yet jumped a game piece.
            if jump_count == 0 and self._board[next_row][next_col] != "   ":
                occupant = self._board[next_row][next_col]
                piece_type = occupant.get_type()
                # Checks if encountered piece is a Cannon.
                if piece_type == "Cannon":
                    return
                jump_count = 1

            self.cannon_moves_list(player, next_row, next_col, r, c, moves, jump_count)


    def cannon_palace_list(self, player, row, column, r, c, moves, jump_count):

        """
        Called by the cannon_moves method. This method defines what moves can be made for these game
        pieces while in the palace. It checks whether a move is valid based on these definitions and where friendly
        and opposing pieces are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :param jump_count: Represents a counter to keep track of whether or not the cannon piece has jumped a piece.
        :return: A list containing lists of valid moves.
        """

        # Checks that the move is in range of the board and if it is valid.
        if row + r in range(3) or row + r in range(7, 10):
            if column + c in range(3, 6):
                next_row = row + r
                next_col = column + c

                # Runs if the Cannon has already jumped a game piece.
                if jump_count == 1:
                    if self._board[next_row][next_col] != "   ":
                        occupant = self._board[next_row][next_col]
                        occ_player = occupant.get_player()
                        piece_type = occupant.get_type()
                        if piece_type == "Cannon" or occ_player == player:
                            if self._board[row][column] != "   ":
                                return
                            moves.append([row, column])
                            return
                        moves.append([next_row, next_col])
                        return
                    moves.append([next_row, next_col])

                # Runs if the Cannon has not yet jumped a game piece.
                if jump_count == 0 and self._board[next_row][next_col] != "   ":
                    occupant = self._board[next_row][next_col]
                    piece_type = occupant.get_type()
                    if piece_type == "Cannon":
                        return
                    jump_count = 1

                self.cannon_palace_list(player, next_row, next_col, r, c, moves, jump_count)


    def soldier_moves(self, piece_obj, player):

        """
        Called by the current_moves method. Defines all possible movements that the Soldier piece can make.
        Calls the soldier_moves_list for each of the game piece's possible movements. Uses the list created by
        the soldier_moves_list method and calls the general_checks method to see if any of the moves in the
        list will put an opposing player's General in check.
        :param piece_obj: Represents a game piece object.
        :param player: Represents the player for the game piece object.
        :return: A list of all valid moves for a game piece object.
        """

        row = piece_obj.get_row()
        column = piece_obj.get_column()
        moves = []

        # Defines specific movements for a Red Soldier
        if player == "RED":
            self.soldier_moves_list(player, row, column, 0, 1, moves)
            self.soldier_moves_list(player, row, column, 0, -1, moves)
            self.soldier_moves_list(player, row, column, 1, 0, moves)

            # Defines specific movements if the game piece is in an opposing players palace.
            if row in range(7, 10) and column in range(3, 6):
                self.soldier_palace_list(player, row, column, 1, 1, moves)
                self.soldier_palace_list(player, row, column, 1, -1, moves)

        # Defines specific movements for a Blue Soldier
        if player == "BLUE":
            self.soldier_moves_list(player, row, column, 0, 1, moves)
            self.soldier_moves_list(player, row, column, 0, -1, moves)
            self.soldier_moves_list(player, row, column, -1, 0, moves)

            # Defines specific movements if the game piece is in an opposing players palace.
            if row in range(0, 3) and column in range(3, 6):
                self.soldier_palace_list(player, row, column, -1, -1, moves)
                self.soldier_palace_list(player, row, column, -1, 1, moves)

        for move in moves:
            self.general_check(move)

        return moves

    def soldier_moves_list(self, player, row, column, r, c, moves):

        """
        Called by the soldier_moves method. This method defines what moves can be made for these game
        pieces. It checks whether a move is valid based on these definitions and where friendly and opposing pieces
        are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """

        # Checks that the move is in range of the board and if it is valid.
        board = self.get_board()
        if row + r in range(10) and column + c in range(9):
            if board[row + r][column + c] != "   ":
                occupant = board[row + r][column + c]
                occ_player = occupant.get_player()
                if occ_player == player:
                    return moves
                moves.append([row + r, column + c])
                return moves
            moves.append([row + r, column + c])

        return moves


    def soldier_palace_list(self, player, row, column, r, c, moves):

        """
        Called by the soldier_moves method. This method defines what moves can be made for these game pieces while in
        the opposing player's palace. It checks whether a move is valid based on these definitions and where friendly
        and opposing pieces are positioned on the current board. If a move is valid it is appended to the moves list.
        :param player: Represents the player that the piece object belongs to.
        :param row: Represents the current of the game piece.
        :param column: Represents the current column of the game piece.
        :param r: Represents the movement along a row for the current game piece as an integer.
        :param c: Represents the movement along a column for the current game piece as an integer.
        :param moves: Represents a list of valid moves containing a list with a row and column.
        :return: A list containing lists of valid moves.
        """

        # Checks that the move is in range of the board and palace and if it is valid.
        board = self.get_board()
        if row + r in range(3) or row + r in range(7, 10):
            if column + c in range(3, 6):
                if board[row + r][column + c] != "   ":
                    occupant = board[row + r][column + c]
                    occ_player = occupant.get_player()
                    if occ_player == player:
                        return moves
                    moves.append([row + r, column + c])
                    return moves
                moves.append([row + r, column + c])
        return moves


    def display_board(self):

        """
        Prints the current game board and pieces in a way that is more representative of an actual game board.
        Uses abbreviations for the piece type and player.
        :return: NONE
        """

        dis_board = self.get_board()
        pieces = self.get_pieces()
        for piece in pieces:
            row = Pieces.get_row(piece)
            column = Pieces.get_column(piece)
            dis_board[row][column] = piece.get_name()

        for row in dis_board:
            print(row)
            print()

