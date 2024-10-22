class TicTacToe:
    def __init__(self, n):
        self.size = n
        self.rowSum = [0] * n
        self.colSum = [0] * n
        self.diagSum = 0
        self.revDiagSum = 0
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.moves = n * n

    def print_board(self):
        """
        prints the current board status
        """
        for row in self.board:
            print(row)

    def check_winner_slow(self, player: int, row: int, col: int):
        """
        Checks if the player wins the game in O(n).

        Parameters:
        player (int): player number.

        Returns:
        (int) player -> if player wins
        (int) -2 -> if no player wins
        """
         # O(n) solution to check if player wins
        winRow , winCol, winDiag, winRevDiag = True, True, True, True

        for i in range(self.size):
            if self.board[i][col] != player:
                winCol = False
            if self.board[row][i] != player:
                winRow = False
            if self.board[i][i] != player:
                winDiag = False
            if self.board[i][self.size - i - 1] != player:
                winRevDiag = False

        if winRow or winCol or winDiag or winRevDiag:
            return player
        
        if self.moves == 0:
            return 0
        
        return -2
    
    def check_winner_fast(self, player: int, row: int, col: int):
        """
        Checks if the player wins the game in O(1).
        works only if players are -1 and 1.

        Parameters:
        player (int): player number.

        Returns:
        (int) player -> if player wins
        (int) -2 -> if no player wins
        """
        # O(1) solution to check if player wins
        self.rowSum[row] += player
        self.colSum[col] += player

        if row == col:
            self.diagSum += player

        if row == self.size - col - 1:
            self.revDiagSum += player

        if abs(self.rowSum[row]) == self.size or abs(self.colSum[col]) == self.size or abs(self.diagSum) == self.size or abs(self.revDiagSum) == self.size:
            return player
        if self.moves == 0:
            return 0
        return -2


    def move(self, row: int, col:int, player: int):
        """
        Makes a move on the board.

        Parameters:
        row (int): move's row index.
        col (int): move's col index.

        Returns:
        (int) player -> if player wins or
        (int) -3 -> if row or col is out of bounds
        (int) -2 -> if move is successful
        """

        if row >= len(self.board) or col >= len(self.board[0]) or row < 0 or col < 0 or self.board[row][col] != 0:
            return -3
        
        self.board[row][col] = player
        self.moves = self.moves - 1

        return self.check_winner_fast(player, row, col)

       

