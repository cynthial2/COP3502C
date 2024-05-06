# Lab 05: Connect-Four

def print_board(array):
    for row, sublist in reversed(list(enumerate(array))):
        for col, cell in enumerate(sublist):
            print(array[row][col], end=' ')
        print()


def initialize_board(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = '-'



def insert_chip(array, col, chip_type):
    for idx, row in enumerate(array):
        if array[idx][col] == '-':
            board[idx][col] = chip_type
            break
    return idx


def check_if_winner(array, col, row, chip_type):
    # Check horizontal
    count = 0
    for item in array[row]:
        if item == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    # Check vertical
    count = 0
    for idx, item in enumerate(array):
        if array[idx][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


if __name__ == '__main__':
    # Set-up board
    height = int(input('What would you like the height of the board to be? '))
    length = int(input('What would you like the length of the board to be? '))

    board = [['' for i in range(length)] for j in range(height)]
    initialize_board(board)
    print_board(board)
    print()

    print('Player 1: x\nPlayer 2: o\n')

    turn = 0
    player = 1
    chip = 'x'

    # Main Game
    while True:
        # Current player casts chip
        choose = int(input(f'Player {player}: Which column would you like to choose? '))
        row_num = int(insert_chip(board, choose, chip))
        print_board(board)
        print()

        # Check if wins
        winner = check_if_winner(board, choose, row_num, chip)
        if winner == True:
            print(f'Player {player} won the game!')
            break

        # Switch player
        turn += 1
        player = 2 if player == 1 else 1
        chip = 'o' if chip == 'x' else 'x'

        # If out of space
        if turn == height*length:
            print('Draw. Nobody wins.')
            break


