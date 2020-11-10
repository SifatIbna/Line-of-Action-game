from board import Game_Board
from search import alphabeta_search
import time

def game(size):
    
    b = Game_Board.init_board(size)
    while True:
        start = time.time()
        print(b)
            
        if (b.is_terminal_state()):
            winner = b.winner()
            if winner == 0:
                print("It's a tie")
            else:
                print('Player {} has won'.format(winner))
            break
            
        b = alphabeta_search(b)
        stop = time.time()
        print("Total Time Taken : {}".format(stop-start))


if __name__ == '__main__':
    print("Lines Of Action")
    print("Enter the board size :")
    size = int(input())
    game(size)
