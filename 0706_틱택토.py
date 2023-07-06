def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # row
            return True
        if all(board[j][i] == player for j in range(3)):  # column
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:  # main diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:  # counter diagonal
        return True
    return False

def solution(board):
    count_O = sum(row.count('O') for row in board)
    count_X = sum(row.count('X') for row in board)
    if not (count_O == count_X or count_O == count_X + 1):
        return 0
    win_O = check_win(board, 'O')
    win_X = check_win(board, 'X')
    if win_O and win_X:
        return 0
    if win_O and count_O != count_X + 1:
        return 0
    if win_X and count_O != count_X:
        return 0
    return 1
