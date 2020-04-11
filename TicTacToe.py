
import random
from itertools import combinations

class Board(object):

    def __init__(self):
        self.board = {x:None for x in (7,8,9,4,5,6,1,2,3)}

    def display(self):

        d_board = '\nTIC TAC TOE:\n'
        for pos, obj in self.board.items():
            if obj == None:
                d_board += '_'
            elif obj == 'X':
                d_board += 'X'
            elif obj == 'O':
                d_board += 'O'

            if pos%3 == 0:
                d_board += '\n'
        print(d_board)

    def getAvailable(self):
        available = []
        for pos, obj in self.board.items():
            if obj == None:
                available.append(pos)
        return available

class Tic_Tac_Toe(Board):
    pieces = ['O', 'X']

    def __init__(self):
        super().__init__()
        self.piece = Tic_Tac_Toe.pieces.pop(random.choice([0,1]))
        self.cp_piece = Tic_Tac_Toe.pieces[0]

    def usrInput(self, position):
        self.board[position] = self.piece

    def user_getPiece(self):
        return self.piece

    def cp_setPiece(self):
        self.board[random.choice(self.getAvailable())] = self.cp_piece

    def cp_getPiece(self):
        return self.cp_piece

    def win(self, player):

        def at_least_one(A, B):
            for i in A:
                for j in B:
                    if i == j:
                        return True
            return False

        winningPatern = [(1,2,3),(4,5,6),(7,8,9),
                        (1,4,7),(2,5,8),(3,6,9),
                        (3,5,7),(1,5,9)]
        spots = [k for k, v in self.board.items() if v == player]
        spots.sort()
        player_combinations = list(combinations(spots,3))
        if at_least_one(player_combinations, winningPatern) == True:
            return True
        return False

    def MainBoard(self):
        if None not in self.board.values():
            self.display()
            print('HOUuSE FuLl')
            return True
        return False


def main():
    # Setup game
    game = Tic_Tac_Toe()
    input('hELLO fRIEnDs : PRESS ENTER TO BEGIN')

    if game.user_getPiece() == 'X':
        print('x IS fIRST.')
    else:
        print('Y IS sECOND.')
        game.cp_setPiece()

    # Main game loop
    while True:
        game.display()
        position = input('Use the number pad on the lefthand side of your keyboard\nto select your position (1-9):')

        try:
            position = int(position)
            if position in range(1,10):
                if position in game.getAvailable():
                    game.usrInput(position)
                else:
                    print('==>Please input an available position.')
                    continue
            else:
                print('==>Please input a number between 1 and 9.')

        except ValueError:
            print('==>Please input a number.')
            continue

        # FOR USER
        # Check for win
        if game.win(game.user_getPiece()) == True:
            game.display()
            print('VICTORY!')
            break

        # Check for full board
        if game.MainBoard() == True:
            break

        # FOR COMPUTER
        game.cp_setPiece()
        # Check for win
        if game.win(game.cp_getPiece()) == True:
            game.display()
            print('Sorry. You lost.')
            break

        # Check for full board
        if game.MainBoard() == True:
            break

if __name__ == '__main__':
    main()
import random
from itertools import combinations

class Board(object):

    def __init__(self):
        self.board = {x:None for x in (7,8,9,4,5,6,1,2,3)}

    def display(self):
        d_board = '\nTIC TAC TOE:\n'
        for pos, obj in self.board.items():
            if obj == None:
                d_board += '_'
            elif obj == 'X':
                d_board += 'X'
            elif obj == 'O':
                d_board += 'O'

            if pos%3 == 0:
                d_board += '\n'
        print(d_board)

    def getAvailable(self):
        available = []
        for pos, obj in self.board.items():
            if obj == None:
                available.append(pos)
        return available

class Tic_Tac_Toe(Board):
    pieces = ['O', 'X']

    def __init__(self):
        super().__init__()
        self.piece = Tic_Tac_Toe.pieces.pop(random.choice([0,1]))
        self.cp_piece = Tic_Tac_Toe.pieces[0]

    def usrInput(self, position):

        self.board[position] = self.piece

    def user_getPiece(self):
        return self.piece

    def cp_setPiece(self):
        self.board[random.choice(self.getAvailable())] = self.cp_piece

    def cp_getPiece(self):
        return self.cp_piece

    def win(self, player):

        def at_least_one(A, B):
            for i in A:
                for j in B:
                    if i == j:
                        return True
            return False

        winningPatern = [(1,2,3),(4,5,6),(7,8,9),
                        (1,4,7),(2,5,8),(3,6,9),
                        (3,5,7),(1,5,9)]
        spots = [k for k, v in self.board.items() if v == player]
        spots.sort()
        player_combinations = list(combinations(spots,3))
        if at_least_one(player_combinations, winningPatern) == True:
            return True
        return False

    def MainBoard(self):
        if None not in self.board.values():
            self.display()
            print('HoUsE FuLL')
            return True
        return False


def main():
    # Setup game
    game = Tic_Tac_Toe()
    input('hELLO fRIEnDs : PRESS ENTER TO BEGIN')

    if game.user_getPiece() == 'X':
        print('x IS fIRST')
    else:
        print('O IS sECONd')
        game.cp_setPiece()

    # Main game loop
    while True:
        game.display()
        position = input('Use the number pad on the lefthand side of your keyboard\nto select your position (1-9):')

        try:
            position = int(position)
            if position in range(1,10):
                if position in game.getAvailable():
                    game.usrInput(position)
                else:
                    print('==>Please input an available position.')
                    continue
            else:
                print('==>Please input a number between 1 and 9.')

        except ValueError:
            print('===>Please input a number.')
            continue

        # FOR USER
        # Check for win
        if game.win(game.user_getPiece()) == True:
            game.display()
            print('WINNER WINNER BEEF DINNER :-)')
            break

        # Check for full board
        if game.MainBoard() == True:
            break

        # FOR COMPUTER
        game.cp_setPiece()
        # Check for win
        if game.win(game.cp_getPiece()) == True:
            game.display()
            print('You lose.')
            break

        # Check for full board
        if game.MainBoard() == True:
            break

if __name__ == '__main__':
    main()
