import math
X = "X"
O = "O"
EMPTY = None
def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    ne=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                ne+=1
            elif board[i][j]==O:
                ne-=1
    if ne==0:
        return X
    else:
        return O

    


def actions(board):
    s=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                s.add((i,j))
    return s
    


def result(board, action):
    a=board.copy()
    if action in actions(board):
        p=player(board)
        a[action[0]][action[1]]=p
    elif terminal(board):
        raise ValueError("Game Over")
    else:
        raise ValueError("It is wrong move,Do you know the rules of the game ?")

        


def winner(board):
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None: 
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    if actions(board)==set():
        return True
    else:
        return False



def utility(board):
    win=winner(board)
    if w==O:
        return -1
    elif w==X:
        return 1
    else:
        return 0



def minimax(board):
    p = player(board)

    # If empty board is provided as input, return corner.
    if board == [[EMPTY]*3]*3:
        return (0,0)

    if p == X:
        v = float("-inf")
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                selected_action = action
    elif p == O:
        v = float("inf")
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                selected_action = action

    return selected_action
def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

