from board import Game_Board
from search import alphabeta_search
import time
from weights import weigths

def game(size):
    
    weights = 0
    weight8,weight6 = weigths()
    
    if size == 6:
        weights = weight6
    elif size == 8:
        weights = weight8
        
    b = Game_Board.init_board(size,weights)
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
        
        if ( b.get_player() == 2):
            
            print("choose the white piece(x)")
            white_piece_number_x = int(input())
            print("choose the white piece(y)")
            white_piece_number_y = int(input())
            
            print("Position to move (x): ")
            position_x = int(input())
            print("Position to move (y): ")
            position_y = int(input())
            
            board = b.get_board()
            board[position_x][position_y] = board[white_piece_number_x][white_piece_number_y]
            board[white_piece_number_x][white_piece_number_y] = 0
            
            b.set_board(board)
            b.set_player(3-b.get_player())
            
            stop = time.time()
            print("Total Time Taken : {}".format(stop-start))
            
            continue
        else:
            b = alphabeta_search(b)
        stop = time.time()
        print("Total Time Taken : {}".format(stop-start))

# def main():
#     print('Lines of Action')
#     game_loop()

if __name__ == '__main__':
    print("Lines Of Action")
    print("Enter the board size :")
    size = int(input())
    game(size)
#     main()
