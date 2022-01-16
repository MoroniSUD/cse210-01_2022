
def main():

    

    #I create the TicTacToe board
    board = [['1','|','2','|','3'],
    ['-','+','-','+','-'],
    ['4','|','5','|','6'],
    ['-','+','-','+','-'],
    ['7','|','8','|','9']
    ]

    print_board(board)

def print_board(board):
    for row in board:
        for i in range(len(row)):
            if i == len(row)-1:
                print(row[i], end='\n')
            else:
                print(row[i], end=' ')      
    return board                

def print_first_board(first_board):
    turn_1 = True
    player_1 = ''
    player_2 = ''
    lap = 0
    while lap < 9:
        if player_1 == '':
            print("Enter the player's name 1 (X):\n")
            player_1 = input()
            print("Enter the player's name 2 (O):\n")
            player_2 = input()
        else:
            if turn_1:
                print(player_1 + ' Select a board position: ') 
            else:
                print(player_2 + ' Select a board position: ')    

            move_player = int(input()) 
    return first_board              

def change_board(board, position, turn_player):
    if turn_player:
        symbol = 'X'
    else:
        symbol = 'O'

    if position == 1:
        if board [0][0] == '1':
            board[0][0] = symbol
            return 0
        else:
            return 'This position is filled'      
    elif position == 2:
        if board [0][2] == '2':
            board[0][2] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 3:
        if board [0][4] == '3':
            board[0][4] = symbol
            return 0
        else:
            return 'This position is filled' 
    elif position == 4:
        if board [2][0] == '4':
            board[2][0] = symbol
            return 0
        else:
            return 'This position is filled' 
    elif position == 5:
        if board [2][2] == '5':
            board[2][2] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 6:
        if board [2][4] == '6':
            board[2][4] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 7:
        if board [4][0] == '7':
            board[4][0] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 8:
        if board [4][2] == '8':
            board[4][2] = symbol
            return 0
        else:
            return 'This position is filled'
    elif position == 9:
        if board [4][4] == '9':
            board[4][4] = symbol
            return 0
        else:
            return 'This position is filled'                                                     
    else:
        return 'This position does not exist.'



# Call main to start this program.
if __name__ == "__main__":
    main()  