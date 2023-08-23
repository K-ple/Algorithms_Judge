def solution(board):
    check0 = 0
    x = len(board)
    for i in board:
        if i.count(0) == 0:
            check0 += 1
    if check0 == len(board):
        return 0
    
    for j in range(x):
        for k in range(x):
            if board[j][k] == 1:
                board[j][k] == 3
                if j>0:
                    if board[j-1][k] != 1:
                        board[j-1][k] = 2
                if j<x-1:
                    if board[j+1][k] != 1:
                        board[j+1][k] = 2
                if k>0:
                    if board[j][k-1] != 1:
                        board[j][k-1] = 2
                if k<x-1:
                    if board[j][k+1] != 1:
                        board[j][k+1] = 2
                if j>0 and k>0:
                    if board[j-1][k-1] != 1:
                        board[j-1][k-1] = 2
                if j>0 and k<x-1:
                    if board[j-1][k+1] != 1:
                        board[j-1][k+1] = 2
                if j<x-1 and k>0:
                    if board[j+1][k-1] != 1:
                        board[j+1][k-1] = 2
                if j<x-1 and k<x-1:
                    if board[j+1][k+1] != 1:
                        board[j+1][k+1] = 2

    answer = 0
    for m in board:
        answer += m.count(0)
    return answer